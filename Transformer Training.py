import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import torchvision as torchV
from torch.utils.data import DataLoader
from torchvision.transforms import Normalize
import math
import copy
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
Data_Compose= torchV.transforms.Compose([torchV.transforms.ToTensor(),Normalize((0.1307,), (0.3081,))])
img_train=torchV.datasets.MNIST(root="dataset",train=True,transform=Data_Compose)
img_test=torchV.datasets.MNIST(root="dataset",train=False,transform=Data_Compose)
img_train_data=DataLoader(dataset=img_train,batch_size=64,shuffle=True,drop_last=False)
img_test_data=DataLoader(dataset=img_test,batch_size=64,shuffle=False,drop_last=False)#这样子数据就加载好了
class MutiAttention(nn.Module):#多头注意力
    def __init__(self,dmodel,number_head):#初始化的时候就要确定有几个头和有几个维度
        super().__init__()#初始化
        assert dmodel % number_head == 0,"维度和注意力头不匹配"
        self.dmodel=dmodel
        self.number_head=number_head#这里用的nn.linear什么的是类,输入进去的是类的初始化参数
        self.dk=dmodel//number_head#算一个头分多少维度
        self.Wq=nn.Linear(dmodel,dmodel)
        self.Wk=nn.Linear(dmodel,dmodel)
        self.Wv = nn.Linear(dmodel, dmodel)#这里算的v
        self.Wo=nn.Linear(dmodel,dmodel)#输出维度一样的
    def split_heads(self,x):#进行每个头的分类和划分
        batch_size,sqe_l,dmodel=x.size()#一个解包赋值语句
        return x.view(batch_size,sqe_l,self.number_head,self.dk).transpose(1,2)
    def attention_dot(self,q,k,v,mask=None):#attention公式计算
        attn_scores=torch.matmul(q,k.transpose(-1,-2))/math.sqrt(self.dk)
        if mask is not None:#现在我们要面对它了，我们要设置mask掩码器
            attn_scores=attn_scores.masked_fill(mask==0,-1e9)#这里为啥乘完之后算也没问题，因为位置索引(列)没变，还是相应位置，只是含义变成了q*k的值
        attn_scores=torch.softmax(attn_scores,dim=-1)#这里的-1也不难理解，就是按照最后一个维度来
        out=torch.matmul(attn_scores,v)
        return out#完成
    def combine_heads(self,x):
        batch_size,_,sqe_l,_=x.size()#还能这么跳过，神了
        return x.transpose(1,2).contiguous().view(batch_size,sqe_l,self.dmodel)#组合完成
    def forward(self,x):
        Q=self.split_heads(self.Wq(x))#调用类内部方法要用self
        K=self.split_heads(self.Wk(x))
        V=self.split_heads(self.Wv(x))
        Out=self.attention_dot(Q,K,V)
        out=self.Wo(self.combine_heads(Out))#组合
        return out#出厂了
class Net(nn.Module):#开始进行网络的拼接
    def __init__(self,dmodel,number_head):
        super().__init__()
        self.flatten = nn.Flatten()
        self.pos_emb = nn.Parameter(torch.randn(1, 28, dmodel))  # 初始化一个可学习的坐标表
        self.MutiAttention=MutiAttention(dmodel,number_head)#进行类的实体化
        self.Conv2d = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=4, stride=1),#但是通过多组滤波器之后算出的矩阵相同
            nn.ReLU(),
            nn.Conv2d(in_channels=6, out_channels=6, kernel_size=4, stride=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # 别忘记池化层也要改变一次矩阵形状
            nn.AdaptiveAvgPool2d((5, 5))  # 这个自适应太牛逼了我去,就不用自己算了
        )  # 这里得把二维的转一维的
        self.lin = nn.Sequential(
            nn.Linear(in_features=784, out_features=20),
            nn.ReLU(),
            nn.Linear(in_features=20, out_features=10)
        )#直接粘贴了，妈的不想自己算了
    def forward(self,x):
        x=x.squeeze(1)#把数组为1的维度挤掉
        x = x + self.pos_emb
        x=self.MutiAttention(x)
        # # x=x.unsqueeze(1)#把维度补上
        # x=self.Conv2d(x)#这玩意只能接受四维的数据
        x=self.flatten(x)#把它拍扁
        x=self.lin(x)
        return x#前向传播完成
model=Net(28,4).to(device)#完成初始化
optimizer=torch.optim.SGD(model.parameters(),lr=0.1)
loss_fn=nn.CrossEntropyLoss()#最后依旧是依靠交叉熵
for i in range(10):#100个epoch
    total_loss = 0
    for x,y in img_train_data:
        x = x.to(device)  # 把图像数据搬到 GPU
        y = y.to(device)  # 把标签也搬到 GPU
        pred=model(x)
        loss=loss_fn(pred,y)
        optimizer.zero_grad()
        total_loss+=loss.item()#tensor数字化
        loss.backward()
        optimizer.step()
    print("loss is",total_loss/len(img_train_data))
total=0
correct=0#要算准确率了
with torch.no_grad():
    for epoch,(x,y) in enumerate(img_test_data):
        x = x.to(device)  # 把图像数据搬到 GPU
        y = y.to(device)  # 把标签也搬到 GPU
        pred=model(x)
        pred_label=pred.argmax(dim=1)
        correct+=(y==pred_label).sum().item()#求出具体数据了
        total+=y.size(0)#把每一个batch_size加起来
print(f"accuracy:{correct/total:4f}")#完成


---
layout: post
title: "求第二大的数"
date: 2026-10-15
categories: algorithm
---

# c语言学习

## 基本知识

* 创建的文件后缀为.c 

* ```c
  #include<stdio.h>
  int main(){
      printf("hello World!");
      return 0;
  }
  ```

* ![image-20260301103823834](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301103823834.png)

  ![image-20260301103920888](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301103920888.png)

![image-20260301104022733](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301104022733.png)

* 预处理表示到底调用的是哪一个库函数，通过更改预处理来实现不同的计算机功能

## 执行流程

![image-20260301105447306](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301105447306.png)

* 组合编译之后生成相应的执行文件

* vscode帮你自动生成相应的文件了
* 编译之后源文件变为obj
* 还要引带相应预处理文件

## 核心语法

![image-20260301105727628](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301105727628.png)

### 注释

![image-20260301105830616](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301105830616.png)

``` c
/*
这个是多行注释
*/
//这个是单行注释
```

* 可用快捷键来加注释的格式
* 通用ctrl+/
* ctrl+k ctrl+c
* obj文件里面注释不参与编译
* 最好不要进行注释嵌套

### 关键字

* 拥有特定含义的英文单词
* 关键字的字母全部小写

![image-20260301111400825](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301111400825.png)

### 常量

![image-20260301111543090](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301111543090.png)

![image-20260301111741632](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301111741632.png)

* 字符常量只有一个，并且只能是字母数字和英文符号，中文不行
* 字符常量不写空值也不行，也会报错

![image-20260301113425766](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301113425766.png)

* 分为两个部分，整型常量和实型常量
* 0在实型常量中可以省略
* 注意计算中间的是计算过程而不是实型常量
* 科学计数法中间不能有空格 

### 输出常量

![image-20260301113950384](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301113950384.png)

![image-20260301114034585](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301114034585.png)

![image-20260301114116950](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301114116950.png)

* 格式控制符也是占位符
* 占位置可以被后面补充内容进行填充
* printf只能打印字符串，打印其他东西需要你使用后面填充字符进行相应的填充

#### 输出多个常量

![image-20260301120035263](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301120035263.png)

* 注意，他们这些数据是一一对应的

#### 输出换行

![image-20260301120212580](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301120212580.png)

```c
printf("1\n");
printf("2");
```

* \r表示回到行首
* \n表示换行
* c给简化了，只要写\n就可以直接进行换行了

* 也可以在同一个printf里面进行换行，在想要换行的位置直接加\n就可以了

## 变量

可变数据

* 变量的生命周期

![image-20260304150246986](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304150246986.png)

![image-20260304150345461](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304150345461.png)

* 只在if的这个大括号中可以使用，出了大括号之后就无法使用了

![image-20260301121915535](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301121915535.png)

![image-20260301121957293](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301121957293.png)

* 数据类型 变量名
* 变量名=数据值;

![image-20260301122124552](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301122124552.png)

* 数据类型 变量名 =数值;

![image-20260301122834389](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301122834389.png)

* 变量可以算数过程来进行赋值，赋值为运算结果
* 变量也可以进行自增自减

vc要求变量同意在开头定义完才型

### 变量的注意事项

![image-20260301142543704](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301142543704.png)

* 重复赋值会被覆盖掉
* 重复定义变量名会导致错误

```c 
int a=10;
int a;
//此时就会报错
```

![image-20260301142823434](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301142823434.png)

int a=10,b=20,c=30;

* 不推荐使用，因为不方便阅读变量的具体数据类型
* 变量使用之前，一定要先进行定义

## 计算机的存储规则

![image-20260301143216392](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301143216392.png)

![image-20260301144503627](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301144503627.png)

* 数字是直接转换
* 字符使用ascall码转换之后进行存储的
* 汉字是用相应的编码转换成二进制进行存储的
* 图片是由一堆像素点来进行存储的，像素点颜色由RGB来进行表示
* 音频通过采样点让数字信号来模拟模拟信号

## 常见进制

* 八进制由3个二进制为一组来进行表示
* 十六进制由4个二进制为一组来进行表示

![image-20260301213822107](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301213822107.png)

![image-20260301213830359](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301213830359.png)

* 赋值完之后都是用10进制的形式进行保存的

![image-20260301213939437](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301213939437.png)

![image-20260301214039765](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301214039765.png)

* 十六进制由0x来表示(零x)
* 二进制由0b来进行表示，后面加上数据
* 八进制由0来进行符号表示

```c
0b1001//注意后面数据要符合相应进制要求
```

### 进制转换

![image-20260301214450102](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301214450102.png)

* 跟数据结构书上交的一个样

![image-20260301214545161](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301214545161.png)

![image-20260301214633781](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301214633781.png)

* 其他进制一个样
* 每一位转为十进制之后再相加

![image-20260301215613686](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301215613686.png)

* 十进制转其他进制用除基取余法

![image-20260301215738226](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301215738226.png)

* 其他进制方法相同

## c语言核心语法2

![image-20260301220710678](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301220710678.png)

![image-20260301220950912](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301220950912.png)

* 数据类型决定存储大小和存储数据的类型

![image-20260301221044415](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301221044415.png)

* 计算机中最小存储单元是一个字节

### c语言中的数据类型

![image-20260301221346461](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301221346461.png)

![image-20260301221922260](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301221922260.png)

![image-20260301222003735](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301222003735.png)

* 表示范围不是一尘不变的，由不同的编译器决定，不同的编译器表示范围都是不同的

![image-20260301222754187](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301222754187.png)

* 要注意其中长整型和超长整型需要在赋值时在后面进行标识，打印时也需要更改占位符格式进行表示

![image-20260301223103329](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260301223103329.png)

* sizeof表示的是每一种数据类型占用多少个字节

```c
printf("%zu",sizeof(int))//可以是关键字，也可以是变量
```

* windows中分别占用字节为2 4 4 8
* 不管是32还是64位的windows都遵循上述字节占用空间

* 整形数据short int中int可以省略，计算机自动识别成short int

![image-20260302100319091](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302100319091.png)

* 注意无符号整型打印时要用%u当占位符来使用
* 无符号的赋值负数是会溢出出错的
* 一旦变为无符号的数据类型时，数字从0开始，大小还是由2 4 8 字节来存储的

### 实型(小数)的数据类型

![image-20260302100912550](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302100912550.png)

* 小数的取值范围比整数大，但到一定大小会失去精度

![image-20260302101002809](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302101002809.png)

![image-20260302101644369](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302101644369.png)

* c语言中小数默认使用double类型，所以在定义float类型时需要在后面加F来进行表示
* 打印时可以用%.3f表示保留小数点后几位(此时这里表示的就是保留小数点后3位置)
* float型最多保留小数点后6位，再多就会失去精度

![image-20260302101911485](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302101911485.png)

* double打印的时候使用lf来进行打印
* 最多精确到小数点后15位

![image-20260302102029770](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302102029770.png)

* 小数的数据类型无法跟unsigned进行组合，unsigned只能和整数类型进行组合

### 字符类型

![image-20260302102327010](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302102327010.png)

* char类型只占一个字节
* char不能存储中文

### 标识符![image-20260302103355880](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302103355880.png)

* 自己起的名字就是标识符，如果是编译器定义好的就叫关键字

![image-20260302103519561](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302103519561.png)

* 数字字母下划线，不能以数字开头

![image-20260302103558787](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302103558787.png)

* 不能是关键字

![image-20260302103654388](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302103654388.png)

### 书写建议

![image-20260302104600419](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302104600419.png)

* 在c语言中关键字全部都是小写的
* 函数名，变量名等我们自己定义的都是标识符

## 键盘录入

![image-20260302112521766](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302112521766.png)

![image-20260302112609432](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302112609432.png)

* 键盘录入，变量前加&

![image-20260302112650350](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302112650350.png)

* scanf可能会出现警告，因为这个键盘输入方法并不安全

### c语言中没有string类型的变量，用char数组的形式来对其进行标识

![image-20260302143619009](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302143619009.png)

* 一个中文默认占用2个字节，而且结尾每个都会自带一个结束字节，自带一个字节

* 所以说赋予内存空间的时候要注意

![image-20260302144451639](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302144451639.png)

* scanf进行输入的时候，需要跟""里面的内容完全一致才可以正常输入，然后占位符的地方来接受信息

### 键盘输入多个数据求和

![image-20260302145146104](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302145146104.png)

![image-20260302145237788](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302145237788.png)

* 注意要一一对应，空格也要打上才行
* %d会一直接受整数，直到不是整数才截至，所以不能用整数来进行间隔

## 运算符

![image-20260302152029079](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302152029079.png)

* 让两个整数参与计算，得到的结果也一定是一个整数，小数点后面部分抛弃而不会进位
* 整数和小数计算，结果一定是一个小数

![image-20260302153630630](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302153630630.png)

* 不能用错误的数学公式进行计算，比如说除数为0

![image-20260302153830577](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302153830577.png)

![image-20260302153915137](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302153915137.png)

* 取余也不能除以0
* 取余的正负和第一个数字是保持一致的

### 数值差分 个 十 百

* 个位通过%10来获取
* 十位通过/10%10来获取
* 百位通过/100来获取

### 隐式转换

* 不同数据类型之间不能直接进行互相运算，需要变为同一数据类型之后才能进行计算

![image-20260302155913836](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302155913836.png)

![image-20260302160122586](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302160122586.png)

* short或者char只要进行计算，就会直接转换为int类型

![image-20260302161018929](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302161018929.png)

* 隐式转换都是小变大

### 强制转换

* 从大到小进行转换

![image-20260302161242915](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302161242915.png)

![image-20260302161250900](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302161250900.png)

* 强制转换时，去掉高位的二进制，只保留低位的二进制

![image-20260302161541344](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302161541344.png)

* 强制转换的时候，对数学式子进行转换需要给数学式子加括号，因为数学式子强转时不会看作一个整体

### 字符相加

* 会将char类型的数据根据ascall码转换为int类型的数据来进行计算

![image-20260302162120082](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302162120082.png)

* 如果这时候再进行强制类型转换，又能转换回字符了
* 不清楚对应的ascall码的时候可以直接用int类型转换一下看看是多少就可以了

### 自增自减运算符

![image-20260302200340836](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302200340836.png)

![image-20260302200426280](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302200426280.png)

![image-20260302201323305](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302201323305.png)

* int b=a++;表示先赋值后加加
* int b=++a;表示先加加后赋值
* 在windows中++前缀优先于后缀，会先进性使用，就跟加了括号一样
* ++后缀会先跟着计算，全部计算完之后再进行自增

![image-20260302202551921](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302202551921.png)

### 赋值运算符

![image-20260302203545918](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302203545918.png)

![image-20260302203605790](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302203605790.png)

* 把左边和右边相加，然后把结果赋值到右边
* 取余的时候不能出现小数
* 使用除法的时候，除数不能出现小数

### 关系运算符

![image-20260302203830457](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260302203830457.png)

* 算式结果只有0或者1
* 抽象出两方直接进行比较就可以了，不用绕远路

### 逻辑运算符

![image-20260303200508668](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303200508668.png)

* 取反符号可以连续使用，每次作用都还是取反
* int a=!!1;表示还是1，取反两次返回原值了

#### 逻辑运算符扩展点

![image-20260303202334785](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303202334785.png)

![image-20260303202414557](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303202414557.png)

* 对于&&来说，当左边为0时，右边不会参与计算
* 对于||来说，当左边为1时，右边便不会参与计算
* 逻辑表达式左右两边可以加算式，甚至可以加函数

### 三元运算符

![image-20260303203845541](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303203845541.png)

* 表达式成立则执行表达式1，不成立则执行表达式2

![image-20260303204015350](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303204015350.png)

### 逗号运算符

![image-20260303204530848](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303204530848.png)

![image-20260303205344631](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303205344631.png)

* 用负号可以直接对常量或者变量进行正负的转换

### 运算符的优先级

* 最基本的运算符，先算乘除后算加减

![image-20260303210249096](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303210249096.png)

![image-20260303210312895](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303210312895.png)

![image-20260303210416101](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303210416101.png)

![image-20260303210549380](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303210549380.png)

* 乘除取余都属于二元运算符	

![image-20260303211952987](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303211952987.png)

## 流程控制语句

![image-20260303212628867](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303212628867.png)

* 控制程序的执行流程

* 顺序结构就是从上往下顺序执行

### 分支结构

![image-20260303213156293](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303213156293.png)

* 程序出现了岔路
* if语句表示在满足一定条件的情况下才会执行程序

![image-20260303213410636](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303213410636.png)

* 在if中，数字有特殊含义，非0数字表示条件成立，0表示条件不成立

![image-20260303215016800](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303215016800.png)

![image-20260303215153864](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303215153864.png)

#### if的第二种格式

![image-20260303215334768](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260303215334768.png)

 #### if的第三种格式

![image-20260304102511244](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304102511244.png)

![image-20260304102520967](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304102520967.png)

* 分支选择最终只能选择一个分支，而不能选取多个分支，有一个分支被选取之后，整个分支判断就结束了

#### switch语句

![image-20260304104353990](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304104353990.png)

* switch不是范围，而是确定的选项，是就是是，不是就不是，没有讨论的范围

![image-20260304104444534](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304104444534.png)

* 执行语句时执行到break则会结束整个判断流程

![image-20260304104558863](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304104558863.png)

* 如果说没有break，会紧接着不断往后进行判断，执行switch中后面的相应语句
* 如果case中所有的条件都没有被选中，则会执行default中的内容

![image-20260304105008217](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304105008217.png)

* case中条件只能是整数或者字符，也可以是变量，但是要求变量也是整数或者字符(小数也不行)
* case中的条件必须唯一，如果相同，那就不知道具体该执行哪一条了
* default可以写在任意位置，不会对结果造成影响
* if可以实现case的相关内容
* case用在有限条件下，if用在范围上
* if在使用时，是从上到下依次进行判断的，而switch是直接找到相应case，比if少了一个从上往下判断的过程，效率更高

#### case穿透

![image-20260304112150628](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304112150628.png)

* 第一次会进行选中，选中之后如果没有break来结束执行，那么就会顺序执行从上往下把后面的case中的语句执行，而不需要进一步进行判断了

### 循环结构

![image-20260304113746374](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304113746374.png)

![image-20260304113801654](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304113801654.png)

![image-20260304113832126](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304113832126.png)

#### for循环

![image-20260304113913430](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304113913430.png)

* for循环中，条件控制语句是在循环体语句执行结束之后再进行执行的
* 执行顺序是，初始化语句，条件判断语句，判断成功后，执行循环体语句，最后执行条件控制语句

![image-20260304114555934](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304114555934.png)

![image-20260304114714124](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304114714124.png)

![image-20260304114814146](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304114814146.png)

* for循环不会重复进行初始化

![image-20260304115024009](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304115024009.png)

#### for循环技巧

![image-20260304120054092](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304120054092.png)

* 顺序求和时也可以用循环来实现
* 比如说等差数列求和

### while循环

![image-20260304152550407](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304152550407.png)

* 执行顺序和for循环执行顺序是完全一样的

![image-20260304152621800](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304152621800.png)

### for和while的区别

![image-20260304152928294](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304152928294.png)

![image-20260304153030771](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304153030771.png)

* 循环执行不知道何时结束的条件时，用while，而数字相关的有限的循环多用for来表示
* 也就是说如果是要循环执行和判断函数，最好用while循环来执行

### while真题

#### 判断整数是否是2的幂次方

![image-20260304153748252](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304153748252.png)

![image-20260304154329136](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304154329136.png)

#### 折纸问题

![image-20260304155106993](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304155106993.png)

![image-20260304155312815](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304155312815.png)

#### 整数反转

![image-20260304160127345](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304160127345.png)

* 注意最后组装，每一步都乘以10，最后组装起来就是正确的
* 每一步取出一个数字后，除以10将该数字去除掉

#### 平凡根

![image-20260304160314783](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304160314783.png)

* 思路是枚举

![image-20260304160512120](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304160512120.png)

![image-20260304160640751](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304160640751.png)

![image-20260304160929951](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304160929951.png)

#### 判断一个整数是否是回文数

![image-20260304161018425](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304161018425.png)

* 先反转后跟原数字进行比较即可，相等就是回文数，不相等就不是回文数

#### 两数相除

![image-20260304161825204](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304161825204.png)

* 对于编程语言来说，除法和乘法都是通过加减来实现的

![image-20260304162018477](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260304162018477.png)

```c
#include <stdio.h>
int main(){
    int diva,divb;
    int count=0;
    scanf("%d %d",&diva,&divb);
    while ((diva-divb)>=0)
    {
        /* code */
        diva-=divb;
        count++;
    }
    printf("%d",count);
    printf("%d",diva);
    }
```

* 做题的时候要先进行数学分析，之后再编写代码

### do....while

![image-20260305103033643](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305103033643.png)

![image-20260305103103101](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305103103101.png)

* 先进行循环，后进行判断

## 循环高级

![image-20260305103352179](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305103352179.png)

* 无限循环可以配合if来使用，这样可以让结束条件正着写，就不用反着来写了

### 跳转控制语句

![image-20260305104629937](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305104629937.png)

![image-20260305104659704](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305104659704.png)

* 在循环中遇见break则会直接结束循环，然后执行后面的代码

![image-20260305105811116](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305105811116.png)

* 会跳过循环体语句，直接执行条件控制语句

### 循环嵌套

![image-20260305110123472](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305110123472.png)

![image-20260305110930675](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305110930675.png)

* 要先确定内循环要做射门么事情，因为内循环是重点，外循环只是内循环执行了n次

![image-20260305111110503](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305111110503.png)

![image-20260305111352263](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305111352263.png)

* 把变量的变换自增自减用外层循环的循环变量来代替实现了

#### 九九乘法表

![image-20260305113304778](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305113304778.png)

![image-20260305113401415](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305113401415.png)

* 用制表符可以让数据对齐表示(\t)

![image-20260305113545314](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305113545314.png)

* 补空格的时候，只能补8个空格的倍数，补空格是补在最后面的
* 中文字符代表了两个字母，所以制表符补充时会补充六个(单字符的时候)

#### 统计质数

![image-20260305113955086](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305113955086.png)

![image-20260305114021612](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305114021612.png)

* 通常这种题的做法都是枚举

* 判断是否能被整除只要进行取余就可以了
* 判断是不是质数只要取考虑是否会被整除就可以了，只要能被1或者这个数本身以外的数整除，那么这个数就不是质数

![image-20260305114725612](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305114725612.png)

### 计算数字

![image-20260305115433824](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305115433824.png)

![image-20260305115947367](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305115947367.png)

### 和为15的数字

![image-20260305150900715](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305150900715.png)

```c
#include <stdio.h>
int main(){
    int number=167;
    int sum=0;
    while (number>0)
    {
        /* code */
        sum+=number%10;
        number=number/10;
    }
    if(sum==15){
        printf("yes");
    }else{
        printf("no");
    }
    }//内层循环代码
```

### 循环嵌套跳出问题

![image-20260305151641501](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305151641501.png)

* break只能跳出单层循环

![image-20260305151922150](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305151922150.png)

* 使用goto语句可以直接跳转到相应标号的位置

![image-20260305152024246](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305152024246.png)

* 跳过去之后就会在标号位置继续顺序执行了

![image-20260305152049833](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305152049833.png)

* 也可以用来进行循环嵌套，但是实在是太晕了，不如用while来实现无线循环

## 函数

![image-20260305152249175](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305152249175.png)

* 避免重复代码，并且是在想用重复代码时才使用，不会被强行进行使用

![image-20260305152459264](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305152459264.png)

![image-20260305153317320](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305153317320.png)

* 定义函数不可以写在main里面，写在里面是会直接报错的

### 带有参数的函数

![image-20260305154124270](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305154124270.png)

![image-20260305154133896](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305154133896.png)

* 只完成功能，不对变量进行赋值

![image-20260305154307254](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305154307254.png)

* 函数定义为形参，自己输入的具体的为实参
* 形参和实参之间数据类型要保持一致

### 函数的返回值

![image-20260305155428921](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305155428921.png)

![image-20260305155436350](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305155436350.png)

* 看返回值是什么类型的，那就给函数设置相应的数据类型
* 也就是说，函数的数据类型是什么类型，是由返回值的数据类型决定的
* 对函数接收时也需要使用相应的数据类型进行接收

![image-20260305155925942](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305155925942.png)

* 只需要对有限的函数进行更改就可以了,所以提高了代码的可维护性

![image-20260305160027338](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305160027338.png)

* 可以用变量接受返回值，也可以直接打印出来

### 定义函数终极绝招

![image-20260305185423024](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305185423024.png)

![image-20260305190207257](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305190207257.png)

* 函数确实是不能嵌套的也就是说在main函数里是不能定义函数的，其他的函数里面也不能定义函数，会直接报错

![image-20260305190615315](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305190615315.png)

* 程序执行定义时是从上往下进行执行的，所以说如果函数定义在下面了，需要在开头进行表明
* 函数中执行到return之后，整个函数会直接结束执行

### 常见函数

![image-20260305190914775](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305190914775.png)

* 根据不同的头文件来调用不同的函数

![image-20260305191449947](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305191449947.png)

![image-20260305191743808](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260305191743808.png)

### time头文件

* 返回值是longlong类型的

![image-20260307100523170](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307100523170.png)

* 返回的是从c语言诞生的生日到现在过了多少秒

![image-20260307100651706](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307100651706.png)

### 随机数

![image-20260307100728329](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307100728329.png)

* 随机数中头文件为#include<stdlib.h>
* C语言中的随机数是伪随机数，不是真正的随机数

![image-20260307100935442](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307100935442.png)

* 根据相应的数字通过相应公式来形成随机数的

![image-20260307101104159](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307101104159.png)

#### 随机数的两个小弊端

![image-20260307101423584](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307101423584.png)

![image-20260307101433800](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307101433800.png)

* 问题1是种子不变，随机数结果固定
* 其二是随机数范围不受掌控

![image-20260307101605186](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307101605186.png)

* 用时间来当作种子，这样就实现了完全随机，因为时间永远在不断变化
* 默认种子为1，不设置种子时自动设置为1

![image-20260307102017426](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307102017426.png)

* 用取余来限制其相应的范围，最后再+1就可以了

![image-20260307102143167](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307102143167.png)

### 猜数小游戏

![image-20260307102721072](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307102721072.png)

![image-20260307103215997](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307103215997.png)

## 数组

![image-20260307103723180](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307103723180.png)

![image-20260307103843269](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307103843269.png)

![image-20260307103858723](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307103858723.png)

### 数组的定义

![image-20260307103928386](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307103928386.png)

![image-20260307104043509](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307104043509.png)

* 数组是再程序建立时先进行空间建立，所以数组的长度并不可以动态改变
* 如果说存储比数组数据类型小的数据也是可以的，通过隐式转换

### 数组的初始化

![image-20260307105013653](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307105013653.png)

![image-20260307105033891](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307105033891.png)

* 没有写数组长度的时候，根据后面的元素个数来自动建立相应长度的数组

![image-20260307105222833](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307105222833.png)

![image-20260307105604059](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307105604059.png)

### 元素访问

![image-20260307110218138](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307110218138.png)

* 索引从0开始

![image-20260307110512609](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307110512609.png)

![image-20260307110546031](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307110546031.png)

### 数组的遍历

![image-20260307110938821](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307110938821.png)

![image-20260307111230421](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307111230421.png)

### 数组地址

![image-20260307112455994](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307112455994.png)

* 没有保存的数据是再内存中进行临时存储的

![image-20260307112552276](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307112552276.png)

* 一个字节8个二进制

![image-20260307112736607](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307112736607.png)

![image-20260307112826333](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307112826333.png)

![image-20260307113010681](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307113010681.png)

* 32位系统只能支持到4GB内存，所以被淘汰了
* 变量内存地址存储的是首地址，然后根据变量具体大小继续往下找就可以了

![image-20260307113303867](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307113303867.png)

* 通过&来换取变量的内存地址
* 通过%p来打印内存地址

### 数组内存地址深度剖析

![image-20260307113700983](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307113700983.png)

* 可以将索引看作是偏移量，是从首地址为开头进行计算的

![image-20260307114148747](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307114148747.png)

* 索引表示的就是偏移量，以0开头是表示偏移量为0

![image-20260307114446570](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307114446570.png)

### 数组常见的两个小问题

![image-20260307115010376](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307115010376.png)

* 函数形参接收到的是变量首地址，而不是变量本身

![image-20260307115655410](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307115655410.png)

![image-20260307115901657](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307115901657.png)

![image-20260307120106787](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307120106787.png)

* 越界之后会访问数组之外的内容，不可知但程序不会直接报错

### 数组练习题

#### 求最值

![image-20260307150651582](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307150651582.png)

![image-20260307150954561](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307150954561.png)

![image-20260307151119938](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307151119938.png)

#### 遍历数组求和

![image-20260307151213785](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307151213785.png)

* int类型数组默认值为0

![image-20260307151628903](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307151628903.png)

* sum一定要赋值，不然数字会用之前内存遗留下来的数值参与计算，可能会导致结果错误

#### 遍历数组求和(升级版)

![image-20260307151849279](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307151849279.png)

![image-20260307152400508](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307152400508.png)

* 不满足条件则等待，方法是把条件写在判断循环体里面

![image-20260307152650667](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307152650667.png)

* 用来判断数组中是否有重复数字

#### 反转数组

![image-20260307153653741](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307153653741.png)

![image-20260307153738457](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307153738457.png)

* 设置一个i和一个j，分别指向数组开头和数组的结尾
* 如果说循环需要多个变量进行循环，需要在循环外设立多个循环，最好用while循环

![image-20260307154314626](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307154314626.png)

#### 打乱数组中的数据

![image-20260307154431602](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307154431602.png)

![image-20260307154809226](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307154809226.png)

#### 基本查找

* 基本查找也就是顺序查找，也就是从0索引开始，从前往后依次进行查找

![image-20260307155254129](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307155254129.png)

![image-20260307155304127](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307155304127.png)

#### 二分查找/折半查找

![image-20260307155437793](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307155437793.png)

![image-20260307155448569](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307155448569.png)

![image-20260307155723584](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307155723584.png)

* 最小索引加最大索引值除以2，然后赋值给mid

![image-20260307155901395](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307155901395.png)

![image-20260307160801952](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307160801952.png)

![image-20260307161051438](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307161051438.png)

* 排序后索引就变了，就没有意义了

#### 插值查找

![image-20260307161355260](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307161355260.png)

![image-20260307161518023](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307161518023.png)

![image-20260307161730520](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260307161730520.png)

#### 分块查找

![image-20260308104735850](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308104735850.png)

![image-20260308104816582](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308104816582.png)

![image-20260308104837120](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308104837120.png)

![image-20260308105140131](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308105140131.png)

* 又被称为哈希查找

#### 冒泡排序

![image-20260308105754335](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308105754335.png)

![image-20260308105823195](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308105823195.png)

* 不进行交换时，循环结束

![image-20260308110021417](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308110021417.png)

* 从右往左比较，比较出来的是最小值。从左往右比较，比较出来的是最大值

![image-20260308110218263](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308110218263.png)

![image-20260308111037236](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308111037236.png)

#### 选择排序

![image-20260308111348459](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308111348459.png)

![image-20260308111646667](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308111646667.png)

![image-20260308112127348](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308112127348.png)

## 指针

![image-20260308112538296](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308112538296.png)

### 定义格式

![image-20260308112649990](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308112649990.png)

* 指针变量中存储的是内存地址
* 不加*表示的就是具体的数据值，而不是内存地址

### 指针的作用

![image-20260308112805327](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308112805327.png)

![image-20260308113006751](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308113006751.png)

* 通过*来获取内存地址中的相应数据
* *p表示内存中所存储的数据，可直接对数据进行修改

![image-20260308113310010](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308113310010.png)

![image-20260308113515420](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308113515420.png)

![image-20260308113714172](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308113714172.png)

* 会将数值当成内存地址

![image-20260308115441818](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308115441818.png)

* 在函数中不再是只能对局部数据进行操作了，可以对其他函数的数据进行操作

![image-20260308115858334](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308115858334.png)

#### 指针的作用(细节)

![image-20260308152528616](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308152528616.png)

![image-20260308152708061](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308152708061.png)

![image-20260308152736215](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308152736215.png)

#### 给函数返回多个值

![image-20260308152828511](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308152828511.png)

![image-20260308153213433](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308153213433.png)

* 通过指针来返回多个数值

#### 将函数结果与计算状态分开

![image-20260308153505862](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308153505862.png)

![image-20260308153541725](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308153541725.png)

![image-20260308153732546](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308153732546.png)

## 指针高级

![image-20260308154517392](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308154517392.png)

![image-20260308154624189](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308154624189.png)

![image-20260308154712520](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308154712520.png)

![image-20260308160220915](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308160220915.png)

![image-20260308160450899](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308160450899.png)

* 指针乘除是内存地址乘除，无意义

### 野指针

![image-20260308160656106](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308160656106.png)![image-20260308161203294](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308161203294.png)

### 没有类型的指针

![image-20260308161402629](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308161402629.png)

* 只能记录地址值

![image-20260308161422178](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308161422178.png)

![image-20260308161616289](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308161616289.png)

![image-20260308161707575](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308161707575.png)

![image-20260308162029101](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308162029101.png)

* 可以用于任意格式的数据交换，在多数据处理时作用很大

### 二级指针和多级指针

![image-20260308162836551](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308162836551.png)

* 指向指针的指针被称作二级指针

![image-20260308162918843](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308162918843.png)

![image-20260308163102360](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308163102360.png)

![image-20260308163138151](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308163138151.png)

![image-20260308163540079](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308163540079.png)

### 数组和指针

![image-20260308163847033](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308163847033.png)

![image-20260308163855531](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308163855531.png)

![image-20260308164247979](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308164247979.png)

### 数组指针的细节

![image-20260308164637090](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308164637090.png)

![image-20260308164737613](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308164737613.png)

![image-20260308164908219](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308164908219.png)

* 如果是&arr，那么表示的就是arr整体，每次加减按照整体字节大小来进行加减

![image-20260308165133304](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308165133304.png)

![image-20260308165602213](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308165602213.png)

### 二维数组

![image-20260308202055791](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308202055791.png)

![image-20260308202124052](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308202124052.png)

![image-20260308202235455](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308202235455.png)

![image-20260308202940010](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308202940010.png)

* 第一种定义时方式要求数组等长

![image-20260308203935427](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308203935427.png)

### 二维数组(指针操作)

![image-20260308204717515](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308204717515.png)

![image-20260308205401143](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308205401143.png)

### 遍历第二种二维数组

![image-20260308205509324](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308205509324.png)

* 第一种方式存储的是具体的一维数组，第二种方式存储的只是数组地址

![image-20260308210058933](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308210058933.png)

### 数组指针和指针数组

![image-20260308210353195](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260308210353195.png)

### 函数指针

![image-20260309103210430](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309103210430.png)

![image-20260309103401816](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309103401816.png)

![image-20260309103450355](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309103450355.png)

#### 函数指针练习

![image-20260309104727282](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309104727282.png)

* 能够灵活的调用相同类型相同形参的函数

![image-20260309104831955](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309104831955.png)

## 字符串

![image-20260309104853569](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309104853569.png)

![image-20260309105011027](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309105011027.png)

* 字符串没有具体数据类型进行存储

![image-20260309105142806](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309105142806.png)

* 字符串结束用\0来表示

![image-20260309105157061](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309105157061.png)

![image-20260309105221937](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309105221937.png)

![image-20260309110925079](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309110925079.png)

![image-20260309111845975](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309111845975.png)

* 会去常量区去看有没有相同的数据，有相同的数据就会直接调用，没有相同数据才会再从常量区创建

![image-20260309112109749](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309112109749.png)

### 遍历字符串

![image-20260309112232146](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309112232146.png)

![image-20260309112535530](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309112535530.png)

![image-20260309112716940](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309112716940.png)

### 字符串数组

![image-20260309112924063](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309112924063.png)

![image-20260309113219371](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309113219371.png)

![image-20260309113332562](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309113332562.png)

### 字符串常用函数

![image-20260309152044484](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309152044484.png)

![image-20260309152130824](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309152130824.png)

* 使用之前需要导入string,.h的库

![image-20260309152344213](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309152344213.png)

![image-20260309152529934](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309152529934.png)

![image-20260309152810185](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309152810185.png)

![image-20260309152940939](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309152940939.png)

![image-20260309153132589](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309153132589.png)

### 用户登录

![image-20260309153201675](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309153201675.png)

![image-20260309153520398](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309153520398.png)

### 统计字符次数

![image-20260309154022650](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309154022650.png)

![image-20260309154453832](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309154453832.png)

## 结构体

![image-20260309154659998](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309154659998.png)

![image-20260309154713280](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309154713280.png)

![image-20260309154815530](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309154815530.png)

![image-20260309155307767](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309155307767.png)

![image-20260309155443012](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309155443012.png)

### 结构体练习

![image-20260309155522883](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309155522883.png)

![image-20260309155850460](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309155850460.png)

### 结构体起别名

![image-20260309161013683](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309161013683.png)

![image-20260309161306190](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309161306190.png)

![image-20260309161330394](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309161330394.png)

### 结构体作为函数的参数进行传递

![image-20260309161509250](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309161509250.png)

![image-20260309161522488](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309161522488.png)

 ![image-20260309204211840](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309204211840.png)

* 结构体变量传参和普通的数据类型传参是一个样的，都是传输的数据而不是地址

![image-20260309204556565](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309204556565.png)

![image-20260309204806914](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309204806914.png)

![image-20260309204835377](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309204835377.png)

* 和普通数据类型运用起来一个样子

### 结构体的嵌套

![image-20260309205144984](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309205144984.png)

![image-20260309205316845](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309205316845.png)

![image-20260309205501250](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309205501250.png)

![image-20260309205750358](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309205750358.png)

### 结构体综合练习(投票选举)

![image-20260309205845588](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309205845588.png)

![image-20260309211307243](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309211307243.png)

### 结构体内存对齐

![image-20260309212302773](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309212302773.png)

![image-20260309212536149](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309212536149.png)

![image-20260309212647898](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309212647898.png)

![image-20260309213734675](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260309213734675.png)

* 在结构体中，小的数据类型往前写能节约内存空间

## 共用体

![image-20260310201853940](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310201853940.png)

![image-20260310202003336](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310202003336.png)

![image-20260310202031048](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310202031048.png)
![image-20260310202051257](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310202051257.png)

* 共用体变量定义时不能重名

![image-20260310202549499](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310202549499.png)

### 共用体特点

![image-20260310202953261](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310202953261.png)

![image-20260310203454472](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310203454472.png)

	### 结构体和共用体的区别

![image-20260310204640094](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310204640094.png)

![image-20260310204737290](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310204737290.png)

## 动态内存分配

* 想在内存中申请多大的内存就可以申请多大的内存

![image-20260310210550378](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310210550378.png)

![image-20260310210619534](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310210619534.png)

* 需要调用stdlib.h这个库

![image-20260310211857743](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310211857743.png)

* 这玩意跟数组一个样，都是连续存储数据，且变量存储的是首地址，并且步长跟变量的数据类型是一样的

![image-20260310212221567](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310212221567.png)

* 无论是扩容还是初始建立，里面的数值都表示的是几个字节
* 不释放掉内存空间，内存是会被长期占用的，所以说要定时释放空间

![image-20260310212423495](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310212423495.png)

### 动态内存分配的小细节

![image-20260310212516872](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260310212516872.png)

* malloc会根据前面变量的数据类型帮你自动进行强转
* 在该程序执行结束之前，所申请的空间会一直存在，如果不进行释放，很有可能会导致内存溢出
* free(指针名) 这里面的指针指向的是申请分配空间的指针
* 空间一旦被释放之后，数据就不可用了
* 如果说用realloc扩容，如果连续空间不够，会重新选一个空间把数据横移然后再进行扩容，所以指针首地址很有可能会改变，原先指针指向的内存会被free掉
* 所以说扩容之后想要释放空间，只需要释放扩容之后的指针即可

## c语言的内存结构

![image-20260311144246356](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311144246356.png)

![image-20260311144423699](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311144423699.png)

* 数组和变量存在是跟函数绑定在一起的，函数入栈则变量和数组存在，函数出栈则变量和数组消失
* 只要是全局变量，不管是变量还是静态数据，都存储在静态区里

![image-20260311145717928](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311145717928.png)

* 在堆里面的数据不会随着函数出栈而消失，所以说在函数里面定义数组用堆malloc来定义然后将指针传出去就能将定义好的数组在外部使用了

## 文件

![image-20260311150715217](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311150715217.png)

*  程序往外写叫做输出流，程序往里读叫做输入流

![image-20260311150858940](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311150858940.png)

* 知道具体路径之后才能进行读写

![image-20260311151015676](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311151015676.png)

* 相对路径是相对于当前项目而言的

![image-20260311151131342](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311151131342.png)

![image-20260311151845577](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311151845577.png)

### 转义字符

![image-20260311152128652](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311152128652.png)

![image-20260311152229452](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311152229452.png)

![image-20260311152300936](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311152300936.png)

![image-20260311152322230](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311152322230.png)

### 读取数据

![image-20260311152817666](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311152817666.png)

* 文件读取定义在stdio.h的头文件中，不需要额外的头文件了

![image-20260311152956645](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311152956645.png)

![image-20260311153036418](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311153036418.png)

* 返回值为文件类型的指针
* 读取的时候会自动往后一个一个的读

![image-20260311153636097](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311153636097.png)

### 读取数据2

![image-20260311154033969](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311154033969.png)

![image-20260311154152189](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311154152189.png)

![image-20260311154417559](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311154417559.png)

### 读取数据3

![image-20260311155213401](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311155213401.png)

* 数组，数组每个数据占多数个字节，大小，路径
* 返回当前读取到的字节个数

![image-20260311155607487](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311155607487.png)

![image-20260311155802900](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311155802900.png)

![image-20260311160002575](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311160002575.png)

* 程序会自动将相邻中文(如果说一次只读一个字节的话)拼接起来展示，如果输出时，字节中间有阻隔没法正常拼接起来，那么就会出现乱码

### 三种写出数据的方式

![image-20260311202808052](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311202808052.png)

![image-20260311202817853](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311202817853.png)

![image-20260311203041687](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311203041687.png)

![image-20260311203145788](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311203145788.png)

![image-20260311203356126](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311203356126.png)

* 分别是，要写入的内容，内容单个数据所占字节大小，一共有多少个数据，要写入哪个文件

![image-20260311203506801](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311203506801.png)

### 多种读写模式

![image-20260311204056021](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311204056021.png)

![image-20260311205017368](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311205017368.png)

![image-20260311205040999](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311205040999.png)

* 这些用来进行二进制的操作

![image-20260311205102114](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311205102114.png)

### 利用代码拷贝文件

![image-20260311205934984](C:\Users\老余\AppData\Roaming\Typora\typora-user-images\image-20260311205934984.png)


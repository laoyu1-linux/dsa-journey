---
layout: post
title: "求第二大的数"
date: 2026-10-15
categories: algorithm
---

## 题目描述

给定一个数组，找出其中第二大的数。

## 我的解题思路

一开始想用排序，但那是 O(n log n)。后来看了题解，发现可以只遍历一次：维护两个变量 `max1` 和 `max2`，每次更新时把旧的 `max1` 给 `max2`。

## 代码实现

``` python
def second_largest(nums):
    max1 = max2 = float('-inf')
    for n in nums:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2 and n != max1:
            max2 = n
    return max2

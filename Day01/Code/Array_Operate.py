# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Array_Operate.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/22 14:17 
"""


# 1.数组的插入、删除、按照下标随机访问操作


class Array_Operate(object):

    def __init__(self, data):
        """数组类初始化方法"""
        self.data = data        # 数据存储list

    def find(self, index):
        """数组的查找方法：
        参数：
            index:将要查找的数据的下标
        返回：
            如果查找成功，则返回找到的数据
            如果查找失败，则返回False
        """
        if index > len(self.data) or index < 0:
            return False
        else:
            print(self.data.pop(index))
            return True

    def insert(self, index, value):
        """
        数组插入数据操作.
        参数：
            index:将要插入的下标
            value：将要插入的数据
        返回：
            如果插入成功，则返回True
            如果插入失败，则返回False
        """
        if index > len(self.data) or index < 0:
            return False
        else:
            self.data.insert(index, value)
            return True

    def insertToTail(self, value):
        """
        直接在数组尾部插入数据.
        参数：
        value:将要插入的数据
        """
        self.data.append(value)

    def printAll(self):
        """打印但钱数组的所有数据"""
        print(self.data)


list1 = [1, 2, 3, 4, 5, 6]          # 建立列表
array01 = Array_Operate(list1)      # 创建数组对象
array01.insertToTail(7)             # 向末尾添加数字7
print(array01.data)                 # 输出数组
array01.insert(4, 66)               # 在索引4处插入数字66
array01.printAll()                  # 输出数组
array01.find(3)                     # 查找索引6的值

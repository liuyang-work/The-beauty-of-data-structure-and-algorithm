# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：SinglyLinkedList.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/23 10:37 
"""
# 1.单链表的插入、删除、查找操作；
# 2.链表中存储的数据类型是Int


class Node(object):

    def __init__(self, data, next_node=None):
        """Node节点的初始化方法.
        参数:
        data:存储的数据
        next:下一个Node节点的引用地址
        """
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        """Node节点存储数据的获取.
        返回:
        当前Node节点存储的数据
        """
        return self.__data

    @data.setter
    def data(self, data):
        """Node节点存储数据的设置方法.
        参数:
        data:新的存储数据
        """
        self.__data = data

    @property
    def next_node(self):
        """获取Node节点的next指针值.
        返回:
        next指针数据
        """
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        """Node节点next指针的修改方法.
        参数:
        next:新的下一个Node节点的引用
        """
        self.__next = next_node


class SinglyLinkedList(object):
    """单向链表"""

    def __init__(self):
        """单向列表的初始化方法."""
        self.__head = None


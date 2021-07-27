# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Array_Queue.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/27 9:28 
"""
from typing import Optional


class ArrayQueue(object):           # 用数组实现队列

    # 初始化队列
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    # 入队操作
    def enqueue(self, item: str) -> bool:
        # 如果队列为空,返回False
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):       # 调整队列元素在数组中的位置
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0

        self._items.insert(self._tail, item)      # 入队
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:              # 如果不是空队列
            item = self._items[self._head]        # 取出队首元素
            self._head += 1                      # 移动head
            return item                         # 返回队首元素
        else:
            return None

    def __repr__(self) -> str:
        return "".join(item for item in self._items[self._head: self._tail])

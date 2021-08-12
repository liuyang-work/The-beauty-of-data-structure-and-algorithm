
# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Skip_List.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/10 14:27 
"""
import random
from typing import Optional
"""
    跳表的一种实现方法，并且存储的是不重复的正整数
"""


class ListNode:

    def __init__(self, data: Optional[int] = None):
        self.data = data    # 节点数据
        self.forwards = []  # 前向指针


class SkipList:
    _MAX_LEVEL = 16

    def __init__(self):
        self._level_count = 1
        self._head = ListNode()
        self._head.forwards = [None] * type(self)._MAX_LEVEL

    def find(self, value: int) -> Optional[ListNode]:
        p = self._head
        for i in range(self._level_count - 1, -1, -1):  # 向下移动一个级别
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]  # 沿水平移动

        return p.forwards[0] if p.forwards[0] and p.forwards[0].data == value else None

    def insert(self, value: int):
        level = self._random_level()
        if self._level_count < level: self._level_count = level
        new_node = ListNode(value)
        new_node.forwards = [None] * level
        update = [self._head] * level  # 更新就像一个prevs列表

        p = self._head
        for i in range(level - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]

            update[i] = p  # 找到了一个上一个

        for i in range(level):
            new_node.forwards[i] = update[i].forwards[i]  # new_node.next = prev.next
            update[i].forwards[i] = new_node  # prev.next = new_node

    def delete(self, value):
        update = [None] * self._level_count
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]
            update[i] = p

        if p.forwards[0] and p.forwards[0].data == value:
            for i in range(self._level_count - 1, -1, -1):
                if update[i].forwards[i] and update[i].forwards[i].data == value:
                    update[i].forwards[i] = update[i].forwards[i].forwards[
                        i]  # 类似于 prev.next = prev.next.next

    def _random_level(self, p: float = 0.5) -> int:
        level = 1
        while random.random() < p and level < type(self)._MAX_LEVEL:
            level += 1
        return level

    def __repr__(self) -> str:
        values = []
        p = self._head
        while p.forwards[0]:
            values.append(str(p.forwards[0].data))
            p = p.forwards[0]
        return "->".join(values)


if __name__ == "__main__":
    l = SkipList()
    for i in range(10):
        l.insert(i)
    print(l)
    p = l.find(7)
    print(p.data)
    l.delete(3)
    print(l)
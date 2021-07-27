# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Linked_Stack.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/27 8:36 
"""
from typing import Optional


# 定义节点
class Node(object):

    def __init__(self, data: int, node_next=None):
        self.data = data
        self.next = node_next


class LinkedStack(object):
    """ 基于单链表的堆栈。
    """
    def __init__(self):
        self._top = None

    # 入栈操作
    def push(self, value: int):
        new_top = Node(value)
        new_top.next = self._top
        self._top = new_top

    # 出栈操作
    def pop(self) -> Optional[int]:
        if self._top:
            value = self._top.data
            self._top = self._top.next
            return value

    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(current.data)
            current = current.next
        return " ".join(f"{nums}" for _ in nums)


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)

# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Linked_Queue.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/27 10:45 
"""
from typing import Optional


class Node:

    def __init__(self, data: str, node_next=None):  # 定义节点类
        self.data = data
        self.next = node_next


class LinkedQueue:

    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def enqueue(self, value: str):
        new_node = Node(value)
        if self._tail:
            self._tail.next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self) -> Optional[str]:
        if self._head:
            value = self._head.data
            self._head = self._head.next
            if not self._head:
                self._tail = None
            return value

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current.next
        return "->".join(value for value in values)


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)

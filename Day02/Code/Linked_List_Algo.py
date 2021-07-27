# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Linked_List_Algo.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/26 15:13 
"""
"""
    1) 反向单向链表 
    2) 检测列表中的循环 
    3) 合并两个已排序的列表 
    4) 从末尾删除第 n 个节点 
    5) 找到中间节点
"""

from typing import Optional


class Node:
    """创建节点类"""
    def __init__(self, data: int, next=None):
        self.data = data
        self._next = next

# 单链表反转
# 请注意，假设输入是一个节点，而不是一个链表。
def reverse(head: Node) -> Optional[Node]:
    reversed_head = None
    current = head
    while current:
        reversed_head, reversed_head._next, current = current, reversed_head, current._next
    return reversed_head


# 检测环
def has_cycle(head: Node) -> bool:
    slow, fast = head, head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next.next
        if slow == fast:
            return True
    return False


# 有序链表合并
def merge_sorted_list(l1: Node, l2: Node) -> Optional[Node]:
    if l1 and l2:
        p1, p2 = l1, l2
        fake_head = Node(None)
        current = fake_head
        while p1 and p2:
            if p1.data <= p2.data:
                current._next = p1
                p1 = p1._next
            else:
                current._next = p2
                p2 = p2._next
            current = current._next
        current._next = p1 if p1 else p2
        return fake_head._next
    return l1 or l2


# 删除倒数第n个节点。假设n大于0
def remove_nth_from_end(head: Node, n: int) -> Optional[Node]:
    fast = head
    count = 0
    while fast and count < n:
        fast = fast._next
        count += 1
    if not fast and count < n:  # 没有那么多节点

        return head
    if not fast and count == n:
        return head._next

    slow = head
    while fast._next:
        fast, slow = fast._next, slow._next
    slow._next = slow._next.next
    return head


def find_middle_node(head: Node) -> Optional[Node]:
    slow, fast = head, head
    fast = fast._next if fast else None
    while fast and fast._next:
        slow, fast = slow._next, fast._next.next
    return slow


def print_all(head: Node):
    nums = []
    current = head
    while current:
        nums.append(current.data)
        current = current._next
    print("->".join(str(num) for num in nums))

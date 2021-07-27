# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Palindrome.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/26 15:06 
"""
import sys
# 引用当前文件夹下的single_linked_list
sys.path.append('singly_linked_list')
from Singly_Linked_List import SinglyLinkedList

def reverse(head):
    reverse_head = None
    while head:
        next = head._next
        head._next = reverse_head
        reverse_head = head
        head = next

    return reverse_head

def is_palindrome(l):
    l.print_all()
    slow = l._head
    fast = l._head
    position = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        position += 1

    reverse_node = reverse(slow)
    head_node = l._head
    is_palin = True
    while (head_node and reverse_node):
        if (head_node.data == reverse_node.data):
            head_node = head_node.next
            reverse_node = reverse_node._next
        else:
            is_palin = False
            break

    return is_palin

if __name__ == '__main__':
    # the result should be False, True, True, True, True
    test_str_arr = ['ab', 'aa', 'aba', 'abba', 'abcba']
    for str in test_str_arr:
        l = SinglyLinkedList()
        for i in str:
            l.insert_value_to_head(i)

        print(is_palindrome(l))




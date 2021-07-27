# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：ArrayStack.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/26 15:29 
"""


class ArrayStack(object):

    def __init__(self):
        self.stack = []  # 初始化栈

    # 判断栈是否为空
    def is_empty(self):
        return len(self.stack) == 0

    # 获取栈中元素个数
    def size(self):
        return len(self.stack)

    # 入栈操作
    def stack_push(self, value):
        self.stack.append(value)

    # 出栈操作
    def stack_pop(self):
        # 先判断栈是否为空，如果不为空弹出栈顶元素，否则打印“栈已为空”，返回None
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("栈已为空！")
            return None

    # 返回栈顶元素
    def get_top(self):
        # 先判断栈是否为空,如果不为空返回栈顶元素，否则返回 None
        if not self.is_empty():
            return self.stack[self.size() - 1]  # 可以改为 return self.items[-1]

        else:
            return None

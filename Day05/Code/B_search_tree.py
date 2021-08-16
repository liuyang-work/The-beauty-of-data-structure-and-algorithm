# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：B_search_tree.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/16 10:40 
"""
from typing import Optional


class TreeNode(object):     # 节点
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None


class BinarySearchTree(object):     # 二叉搜索树
    def __init__(self):
        self.root = None

    def find(self, value: int):     # 查找
        node = self.root    # 从根节点开始
        while node and node.val != value:
            node = node.left if node.val > value else node.right    # 值小往左子树查找，值大往右子树查找
        return node

    def insert(self, value: int):   # 插入
        if not self.root:
            self.root = TreeNode(value)
            return
        parent = None
        node = self.root
        while node:     # 找到插入的位置
            parent = node
            node = node.left if node.val > value else node.right
        new_node = TreeNode(value)
        if parent.val > value:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, value: int):   # 删除
        node = self.root
        parent = None
        while node and node.val != value:
            parent = node
            node = node.left if node.val > value else node.right
        if not node:
            return

        # 要删除的节点有两个子节点
        if node.left and node.right:
            successor = node.right
            successor_parent = node
            while successor.left:
                successor_parent = successor
                successor = successor.left
            node.val = successor.val
            parent, node = successor_parent, successor

        # 删除节点是叶子节点或者只有一个子节点
        child = node.left if node.left else node.right
        if not parent:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child

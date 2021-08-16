# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Binary_search_tree.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/13 13:26 
"""
from queue import Queue
import math


class TreeNode(object):  # 节点
    def __init__(self, val=None):
        self.val = val  # 值
        self.left = None  # 左子树
        self.right = None  # 右子树
        self.parent = None  # 父亲节点


class BinarySearchTree(object):
    def __init__(self, val_list=None):
        if val_list is None:
            val_list = []
        self.root = None  # 根节点置空
        for n in val_list:  # 初始化树
            self.insert(n)

    def insert(self, data):
        p = None
        """插入节点"""
        assert (isinstance(data, int))
        if self.root is None:  # 如果根节点为空
            self.root = TreeNode(data)  # 把当前节点作为根节点
        else:
            n = self.root  # 树不为空，从根节点开始搜索
            while n:  # 直到节点无子节点
                p = n
                if data < n.val:  # 值小于节点往左边搜索
                    n = n.left
                else:
                    n = n.right  # 值大于节点往右边搜索

            new_node = TreeNode(data)  # 确定节点关系
            new_node.parent = p

            if data < p.val:
                p.left = new_node
            else:
                p.right = new_node
        return True

    def search(self, data):
        """
            搜索返回bst中所有值为data的节点列表
        """
        assert (isinstance(data, int))

        # 所有搜索到的节点
        ret = []

        n = self.root
        while n:
            if data < n.val:
                n = n.left
            else:
                if data == n.val:  # 搜索到的节点加入ret中
                    ret.append(n)
                n = n.right
        return ret

    def delete(self, data):
        """删除"""
        assert (isinstance(data, int))

        # 通过搜索得到需要的节点
        del_list = self.search(data)

        for n in del_list:
            # 父节点为空，又不是根节点，已经不在树上，不用再删除
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)

    def _del(self, node):
        """
            删除
            所删除的节点N存在以下情况：
            1. 没有子节点：直接删除N的父节点指针
            2. 有一个子节点：将N父节点指针指向N的子节点
            3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
            :param data:
            :return:
        """
        # case1
        if node.left is None and node.right is None:  # 如果节点是叶子节点或者只有一个根节点
            # 情况1和2，根节点和普通节点的处理方式不同
            if node == self.root:  # 如果是根节点直接置空
                self.root = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = None
                else:
                    node.parent.right = None

        # case2
        elif node.left is None and node.right is not None:  # 节点只有一个右子节点
            if node == self.root:  # 如果节点是根节点且只有一个右节点
                self.root = node.right
                self.root.parent = None
                node.right = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.left

                node.right.parent = node.parent
                node.parent = None
                node.right = None

        elif node.left is not None and node.right is None:  # 节点只有一个左子节点
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                node.left = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                node.left.parent = node.parent
                node.parent = None
                node.left = None

        # case3
        else:
            min_node = node.right
            # 找出右子树的最小值节点
            if min_node.left:
                min_node = min_node.left

            if node.val != min_node.val:
                node.val = min_node.val
                self._del(min_node)
            # 右子树的最小值节点与被删除节点的值相等，再次删除原节点
            else:
                self._del(min_node)
                self._del(node)

    def get_min(self):
        """返回最小值节点"""
        if self.root is None:
            return None

        n = self.root
        while n.left:  # 左子树不为空，一直往左搜索树
            n = n.left
        return n.val

    def get_max(self):
        """返回最大节点"""
        if self.root is None:
            return None

        n = self.root
        while n.right:  # 右子树不为空，一直往右搜索树
            n = n.right
        return n.val

    def in_order(self):
        """中序遍历"""
        if self.root is None:
            return []

        return self._in_order(self.root)

    def _in_order(self, node):
        if node is None:
            return []

        ret = []
        n = node
        ret.extend(self._in_order(n.left))  # 先左后父再右
        ret.append(n.val)
        ret.extend(self._in_order(n.right))

        return ret

    def __repr__(self):
        # 以字符串形式输出中序遍历
        print(str(self.in_order()))
        return self._draw_tree()

    def _bfs(self):
        """广度优先搜索，通过父子关系记录接节点标号"""
        if self.root is None:
            return []

        ret = []
        q = Queue()
        # 队列[节点，编号]
        q.put(self.root, 1)

        while not q.empty():
            n = q.get()

            if n is not None:
                ret.append((n[0].val, n[1]))
                q.put((n[0].left, n[1]*2))
                q.put((n[0].right, n[1]*2+1))

        return ret

    def _draw_tree(self):
        """可视化"""
        nodes = self._bfs()

        if not nodes:
            print("这是一棵空树")
            return

        layer_num = int(math.log(nodes[-1][-1], 2)) + 1
        prt_nums = []

        for i in range(layer_num):
            prt_nums.append([None]*2**i)

        for v, p in nodes:
            row = int(math.log(p, 2))
            col = p % 2 ** row
            prt_nums[row][col] = v

        prt_str = ''
        for i in prt_nums:
            prt_str += str(i)[1:-1] + '\n'

        return prt_str


if __name__ == "__main__":

    nums = [4, 2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    print(bst)

    # 插入
    bst.insert(1)
    bst.insert(4)
    print(bst)

    # 搜索
    for n in bst.search(2):
        print(n.parent.val, n.val)

    # 删除
    bst.insert(6)
    bst.insert(7)
    print(bst)
    bst.delete(7)
    print(bst)
    bst.delete(6)
    print(bst)
    bst.delete(4)
    print(bst)

    # min max
    print(bst.get_max())
    print(bst.get_min())

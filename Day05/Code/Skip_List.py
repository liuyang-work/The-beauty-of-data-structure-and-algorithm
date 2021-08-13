# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Skip_List.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/10 14:27 
"""
import random


class skip_list_node(object):
    def __init__(self, value, high=1):
        # 节点存储的值
        self.data = value
        # 节点对应索引层的深度
        self.deeps = [None] * high


class skip_list(object):
    """
         跳表的一种实现方法。
         跳表中储存的是不重复的正整数
     """

    def __init__(self):
        # 索引层的最大深度
        self.MAX_LEVEL = 16
        # 跳表的高度
        self.high = 1
        # 每一索引层的首节点，默认值为None
        self.head = skip_list_node(None, self.MAX_LEVEL)

    def find(self, value):
        cur = self.head
        # 从索引的顶层, 逐层定位要查找的值
        # 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
        for i in range(self.high - 1, -1, -1):
            # 同一索引层内, 查找小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < value:
                cur = cur.deeps[i]

        if cur.deeps[0] and cur.deeps[0].data == value:
            return cur.deeps[0]
        return None

    def insert(self, value):
        """
            新增时, 通过随机函数获取要更新的索引层数,
            要对低于给定高度的索引层添加新结点的指针
        """
        high = self.randomLevel()
        if self.high < high:
            self.high = high

        # 申请新节点
        newNode = skip_list_node(value, high)
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [self.head] * high
        cur = self.head

        # 低于随机高度的每一个索引层寻找小于插入值的节点
        for i in range(high - 1, -1, -1):
            # 每个索引层内寻找小于待插入值的节点
            # 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < value:
                cur = cur.deeps[i]
            cache[i] = cur
        # 在小于高度的每个索引层中插入新节点
        for i in range(high):
            newNode.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = newNode

    def delete(self, value):
        """
        删除时，要将每个索引层中对应的节点都删除
        """
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * self.high
        cur = self.head
        # 缓存每一个索引层定位小于插入值的节点
        for i in range(self.high - 1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < value:
                cur = cur.deeps[i]
            cache[i] = cur
        # 如果给定的值存在, 更新索引层中对应的节点
        if cur.deeps[0] and cur.deeps[0].data == value:
            for i in range(self.high):
                if cache[i].deeps[i] and cache[i].deeps[i].data == value:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]

    def randomLevel(self, p=0.25):  # 随机函数，平衡索引层
        high = 1
        for _ in range(self.MAX_LEVEL - 1):
            if random.random() < p:
                high += 1
        return high

    def __repr__(self): # 重写输出方式
        values = []
        p = self.head
        while p.deeps[0]:
            values.append(str(p.deeps[0].data))
            p = p.deeps[0]
        return '->'.join(values)


if __name__ == "__main__":
    test1 = skip_list()
    for i in range(100):
        test1.insert(i)
    print(test1)
    p = test1.find(8)
    print(p.data)
    test1.delete(37)
    print(test1)
    test1.delete(37.5)
    print(test1)

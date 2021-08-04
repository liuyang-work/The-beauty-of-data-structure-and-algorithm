# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Counting_Sort.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/4 8:57 
"""
# 计数排序
from typing import List
import itertools


def counting_sort(a: List[int]):
    if len(a) <= 1:
        return

    # a中有counts[i]个数不大于i
    # 定义一个列表，用于统计每个元素出现的次数
    counts = [0] * (max(a) + 1)
    for num in a:
        counts[num] += 1

    # 顺序累加
    counts = list(itertools.accumulate(counts))

    # 临时数组，存储排序之后的结果
    a_sorted = [0] * len(a)
    for num in reversed(a):
        index = counts[num] - 1
        a_sorted[index] = num
        counts[num] -= 1

    a[:] = a_sorted


if __name__ == "__main__":
    a1 = [1, 2, 3, 4]
    counting_sort(a1)
    print(a1)

    a2 = [1, 1, 1, 1]
    counting_sort(a2)
    print(a2)

    a3 = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7]
    counting_sort(a3)
    print(a3)

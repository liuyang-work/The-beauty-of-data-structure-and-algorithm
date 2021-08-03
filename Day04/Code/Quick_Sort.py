# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Quick_Sort.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/3 13:44 
"""
from typing import List
import random


def quick_sort(a: List[int]):
    _quick_sort_between(a, 0, len(a) - 1)


def _partition(a, low, high):
    pivot, j = a[low], low               # pivot 记录起始点的值，j 记录索引
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]     # 交换
    a[low], a[j] = a[j], a[low]
    return j


def _quick_sort_between(a: List[int], low: int, high: int):
    if low < high:
        # 获得一个随机位置作为支点（区分点）
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]       # 把区分点放在起点，利于遍历数组

        m = _partition(a, low, high)    # a[m] 处于最终位置
        _quick_sort_between(a, low, m - 1)      # 进入递归
        _quick_sort_between(a, m + 1, high)


def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)

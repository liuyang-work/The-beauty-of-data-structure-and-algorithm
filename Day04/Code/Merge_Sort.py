# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Merge_Sort.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/3 10:41 
"""
from typing import List


def merge_sort(a: List[int]):
    _merge_sort_between(a, 0, len(a) - 1)


def _merge_sort_between(a: List[int], low: int, high: int):
    # low指向起始，high指向末尾
    if low < high:
        mid = low + (high - low) // 2  # 中间区分位置
        _merge_sort_between(a, low, mid)  # 左边排序
        _merge_sort_between(a, mid + 1, high)  # 右边排序
        _merge(a, low, mid, high)  # 合并


def _merge(a: List[int], low: int, mid: int, high: int):
    # a[low:mid], a[mid+1:high] 已经排序好
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:  # 合并排序好的数组
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j  # 如果一个区间没有了，剩下的全部合并即可
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp  # 拷贝到原数组


def test_merge_sort():
    a1 = [3, 5, 6, 7, 8]
    merge_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    merge_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    merge_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    test_merge_sort()
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)

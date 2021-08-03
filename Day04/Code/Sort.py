# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Sort.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/3 8:18 
"""


# 冒泡排序
def bubble_sort(a: list[int]):
    length = len(a)  # 获取数组长度
    if length <= 1:
        return

    for i in range(length):
        made_swap = False
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # 交换数据
                made_swap = True
        if not made_swap:
            break


# 插入排序
def insertion_sort(a: list[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(1, length):
        value = a[i]
        j = i - 1  # 标记已排序区间末尾的数
        while j >= 0 and a[j] > value:  # 移动数据
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value  # 插入


# 选择排序
def selection_sort(a: list[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        min_index = i  # 标记最小值索引
        min_val = a[i]  # 存储最小值
        for j in range(i, length):  # 找出最小值
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
    a[i], a[min_index] = a[min_index], a[i]


# 算法测试
def test_bubble_sort():
    test_array = [1, 1, 1, 1]
    bubble_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_insertion_sort():
    test_array = [1, 1, 1, 1]
    insertion_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_selection_sort():
    test_array = [1, 1, 1, 1]
    selection_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insertion_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    selection_sort(array)
    print(array)

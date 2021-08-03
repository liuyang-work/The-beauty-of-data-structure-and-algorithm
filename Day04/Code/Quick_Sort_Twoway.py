# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Quick_Sort_Two.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/3 16:09 
"""
import random


def QuickSort(array):
    # 双向排序: 提高非随机输入的性能
    # 不需要额外的空间,在待排序数组本身内部进行排序
    # 基准值通过random随机选取
    # 入参: 待排序数组, 数组开始索引 0, 数组结束索引 len(array)-1
    if array is None or len(array) < 1:
        return array

    def swap(array, low, upper):
        tmp = array[low]
        array[low] = array[upper]
        array[upper] = tmp
        return array

    def QuickSort_TwoWay(array, low, upper):
        # 小数组排序i可以用插入或选择排序
        # if upper-low < 50 : return arr
        # 基线条件: low index = upper index; 也就是只有一个值的区间
        if low >= upper:
            return array
        # 随机选取基准值，并将基准值替换到数组第一个元素
        swap(array, low, int(random.uniform(low, upper)))
        temp = array[low]
        # 缓存边界值，从上下边界同时排序
        i, j = low, upper
        while True:
            # 第一个元素是基准值,所以要跳过
            i += 1
            # 在小区间中, 进行排序
            # 从下边界开始寻找大于基准值的索引
            while i <= upper and array[i] <= temp:
                i += 1
            # 从上边界开始寻找小于基准值的索引
            # 因为j肯定大于i, 所以索引值肯定在小区间中
            while array[j] > temp:
                j -= 1
            # 如果小索引大于等于大索引, 说明排序完成, 退出排序
            if i >= j:
                break
            swap(array, i, j)
        # 将基准值的索引从下边界调换到索引分割点
        swap(array, low, j)
        QuickSort_TwoWay(array, low, j - 1)
        QuickSort_TwoWay(array, j + 1, upper)
        return array

    return QuickSort_TwoWay(array, 0, len(array) - 1)


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    QuickSort(a1)
    print(a1)
    QuickSort(a2)
    print(a2)
    QuickSort(a3)
    print(a3)
    QuickSort(a4)
    print(a4)

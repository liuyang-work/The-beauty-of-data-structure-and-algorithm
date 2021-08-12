# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：The_Ten_Sorting_Algorithm_Summarizes.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/4 11:01 
"""
import random
from collections import deque
"""
十大排序算法总结：
1.冒泡排序     (Bubbling sort)
2.选择排序     (Select Sort)
3.插入排序     (Insert Sort)
4.希尔排序     (Hill sort)
5.归并排序     (Merge sort)
6.快速排序     (Quick sort)
7.堆排序       (Heap sort )
8.计数排序     (Counting sort)
9.桶排序       (Bucket sort)
10.基数排序    (Cardinality sorting)
"""


# 所有测试数据以正整数为例
# 用列表存储数据
# a = [9,8,7,1,2,3,6,5,4]


# 冒泡排序(Bubbling sort)###################################################
def bubbling_sort(arr):
    if len(arr) <= 1:  # 数组只有一个数或者为空
        return arr
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):  # 每一轮都是从第一个数开始遍历数组
            if arr[j] > arr[j + 1]:  # 如果第一个数大于第二个
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换数据


###########################################################################


# 选择排序(Select Sort)#####################################################
def select_sort(arr):
    if len(arr) <= 1:  # 数组只有一个数或者为空
        return arr

    for i in range(0, len(arr)):  # 最小元素的存放位置
        if i == len(arr) - 1:  # 当循环到最后一个位置时，已经排序好，退出循环
            break
        for j in range(i + 1, len(arr)):  # 从剩余的数据中选出最小值
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]  # 放到已排序好的数据末尾


###########################################################################


# 插入排序(Insertion Sort)##################################################
def insertion_sort(arr):
    if len(arr) <= 1:  # 数组只有一个数或者为空
        return arr

    for i in range(1, len(arr)):  # 假定第一个元素已为有序
        tag = i  # 为实现倒序给一个标签
        tmp = arr[i]
        while arr[tag - 1] > tmp:  # 在有序部分寻找插入位置
            arr[tag] = arr[tag - 1]
            tag -= 1
            if tag == 0:
                break
        arr[tag] = tmp  # 插入


###########################################################################


# 希尔排序(Shell Sort)######################################################
def shell_sort(arr):
    length = len(arr)  # 数组的长度
    gap = length // 2  # 选择增量为length/2,
    while gap > 0:
        for i in range(gap, length):  # 排序每一组
            temp = arr[i]
            preIndex = i - gap
            while preIndex >= 0 and arr[preIndex] > temp:  # 交换排序
                arr[preIndex + gap] = arr[preIndex]
                preIndex -= gap
            arr[preIndex + gap] = temp
        gap //= 2  # 持续缩小增量
    return arr


###########################################################################


# 归并排序(Merge Sort)######################################################
def merge_sort(arr):
    merge_sort_divide(arr, 0, len(arr) - 1)


def merge_sort_divide(arr, start, end):
    # start 指向数列开始，end 指向数列的结尾
    if start < end:  # 拆分数列，直到都拆成一个数为止
        mid = start + (end - start) // 2  # 找出拆分中点
        merge_sort_divide(arr, start, mid)  # 递归拆分
        merge_sort_divide(arr, mid + 1, end)
        merge(arr, start, mid, end)  # 有序合并


def merge(arr, start, mid, end):
    i, j = start, mid + 1  # 拆分后的两个数列的起点
    tmp_array = []
    while i <= mid and j <= end:  # 从两个数组从小到大中取出数据
        if arr[i] <= arr[j]:
            tmp_array.append(arr[i])
            i += 1
        else:
            tmp_array.append(arr[j])
            j += 1
    start_tmp = i if i <= mid else j  # 把剩下的一次性添加到数组
    end_tmp = mid if i <= mid else end
    tmp_array.extend(arr[start_tmp:end_tmp + 1])
    arr[start:end + 1] = tmp_array


###########################################################################


# 快速排序(Quick Sort)#######################################################
def quick_sort(arr):  # arr表示数组
    quick_sort_between(arr, 0, len(arr) - 1)


def quick_sort_partition(arr, start, end):
    pivot, j = arr[start], start  # pivot记录起始点的值，j记录索引
    for i in range(start + 1, end + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]  # 交换
    arr[start], arr[j] = arr[j], arr[start]
    return j


def quick_sort_between(arr, start, end):
    if start < end:
        # 随机挑选基准值（pivot）
        pivot = random.randint(start, end)  # 从数组索引中选出一个作为基准点
        arr[start], arr[pivot] = arr[pivot], arr[start]

        mid = quick_sort_partition(arr, start, end)
        quick_sort_between(arr, start, mid - 1)
        quick_sort_between(arr, mid + 1, end)


############################################################################


# 堆排序 (Heap sort ) ######################################################
def heap_sort(arr):
    length = len(arr) - 1
    first_sort_count = length // 2
    for i in range(first_sort_count):   # 把序列调整为大顶堆
        heap_adjust(arr, first_sort_count - i, length)

    for i in range(length - 1):
        arr = swap_param(arr, 1, length - i)    # 把堆顶元素和堆末尾的元素交换，然后把剩下的元素调整为一个大根堆
        heap_adjust(arr, 1, length - i - 1)

    return [arr[i] for i in range(1, len(arr))]


def heap_adjust(arr, start, end):
    temp = arr[start]
    i = start
    j = 2 * i
    while j <= end:
        if j < end and arr[j] < arr[j + 1]:
            j += 1
        if temp < arr[j]:
            arr[i] = arr[j]
            i = j
            j = 2 * i
        else:
            break
    arr[i] = temp


def swap_param(arr, i, j):  # 交换堆顶和堆底节点
    arr[i], arr[j] = arr[j], arr[i]
    return arr
###########################################################################


# 计数排序(Counting sort)######################################################
def counting_sort(arr):
    if len(arr) <= 1:
        return arr

    maxVal = max(arr)
    countArr = [0 for _ in range(maxVal + 1)]
    for i in arr:
        countArr[i] += 1
    for i in range(1, len(countArr)):
        countArr[i] += countArr[i - 1]
    res = [0 for _ in range(len(arr))]
    for i in range(len(arr) - 1, -1, -1):
        res[countArr[arr[i]] - 1] = arr[i]
        countArr[arr[i]] -= 1
        # 必须要减1，由于待排序元素在res中的位置是由计数数组的值来决定的。
        # 当遍历了元素x之后，小于x的元素不会受影响，大于x的元素不会受影响，
        # 只有等于x的元素会受影响，在往res中压的时候，要比x的位置往前移动一位，
        # 因此需要将计数数组中的下标为x的值减1，使得下次在遍历到x的时候，
        # 压入的位置在前一个x的位置之前
    return res


###########################################################################

# 桶排序(Bucket Sort)######################################################
def bucket_sort(arr):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    # 桶的大小
    bucket_range = (max_num - min_num) / len(arr)
    # 桶数组
    count_list = [[] for _ in range(len(arr) + 1)]
    # 向桶数组填数
    for i in arr:
        count_list[int((i - min_num) // bucket_range)].append(i)
    arr.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            arr.append(j)


###########################################################################


# 基数排序(Cardinality Sorting)######################################################
def get_bite(num, i):  # 获取元素第i位的数
    return (num % (i * 10) - (num % i)) // i


def getMax(numList):  # 获取数组中的最大值
    if len(numList) == 1:
        return numList[0]
    maxNum = numList[0]
    for i in range(len(numList)):
        if numList[i] > maxNum:
            maxNum = numList[i]
    return maxNum


def cardinality_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    maxNum = getMax(arr)
    bitCount = 0
    index = 1
    while maxNum // index:
        bitCount += 1
        index *= 10
    currentBit = 1
    # 统计一下最大值的bitCount（有多少位），因为比较多少次，是有最大值的位数决定的
    while currentBit <= 10 ** (bitCount - 1):  # 开始循环的进行每一个位的比较
        res = []
        buckets = [[] for _ in range(10)]  # 桶排序
        for i in arr:
            currentBitNum = get_bite(i, currentBit)
            buckets[currentBitNum].append(i)
        for i in range(10):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
        arr = res
        currentBit *= 10
    return arr


###########################################################################


# 算法测试
# 冒泡排序测试
def bubbling_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    bubbling_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("冒泡排序后的结果：\n")
    print(array_test)


# 选择排序测试
def select_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    select_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("选择排序后的结果：\n")
    print(array_test)


# 插入排序测试
def insertion_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    insertion_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("插入排序后的结果：\n")
    print(array_test)


# 希尔排序测试
def shell_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    shell_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("希尔排序后的结果：\n")
    print(array_test)


# 归并排序测测试
def merge_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    merge_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("归并排序后的结果：\n")
    print(array_test)


# 快速排序测试
def quick_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    quick_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("快速排序后的结果：\n")
    print(array_test)


# 堆排序测试
def heap_sort_test():
    array_test = deque([9, 8, 7, 1, 2, 3, 6, 5, 4])
    array_test.appendleft(0)
    heap_sort(array_test)
    array_test = list(array_test)
    array_test.pop(0)
    print("堆排序后的结果：\n")
    print(list(array_test))


# 桶排序测试
def bucket_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    bucket_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("桶排序后的结果：\n")
    print(array_test)


# 计数排序
def counting_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    array_test = counting_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("计数排序后的结果：\n")
    print(array_test)


# 基数排序测试
def cardinality_sort_test():
    array_test = [9, 8, 7, 1, 2, 3, 6, 5, 4]
    array_test = cardinality_sort(array_test)
    assert array_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("基数排序后的结果：\n")
    print(array_test)


if __name__ == "__main__":  # 测试算法

    bubbling_sort_test()        # 冒泡排序
    select_sort_test()          # 选择排序
    insertion_sort_test()       # 插入排序
    shell_sort_test()           # 希尔排序
    merge_sort_test()           # 归并排序
    quick_sort_test()           # 快速排序
    heap_sort_test()            # 堆排序
    bucket_sort_test()          # 桶排序
    counting_sort_test()        # 计数排序
    cardinality_sort_test()     # 基数排序

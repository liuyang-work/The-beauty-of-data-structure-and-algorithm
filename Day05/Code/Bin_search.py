# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Bin_search.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/9 8:25 
"""


# 简单的二分查找算法,循环实现
def bin_research(arr, n, value):  # arr 是数组，n 是数组长度，value 是需要查找的值
    low = 0  # 起点索引
    high = n - 1  # 末尾索引

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            print('查找成功,它的索引为' + str(mid))
            print("它的值为:")
            return value
        if arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# 简单的二分查找算法,递归实现
def bin_research_change(arr, n, value):
    return bin_search_internally(arr, 0, n - 1, value)


def bin_search_internally(arr, low, high, value):
    if low > high:
        return -1

    mid = low + ((high - low) >> 1)
    if arr[mid] == value:
        print('查找成功,它的索引为' + str(mid))
        print("它的值为:")
        return value
    elif arr[mid] < value:
        return bin_search_internally(arr, mid + 1, high, value)
    else:
        return bin_search_internally(arr, low, mid - 1, value)


# 二分查找变形 1.查找第一个值等于给定值的元素
def bin_research1(arr, n, value):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        elif mid == 0 or arr[mid - 1] != value:  # mid == 0 那这个元素已经是数组的第一个元素，那它肯定是我们要找的
            print('查找成功,它的索引为' + str(mid))
            print("它的值为:")
            return value  # 如果 mid 不等于 0，但 a[mid] 的前一个元素 a[mid-1] 不等于value，
            # 那也说明 a[mid] 就是我们要找的第一个值等于给定值的元素。
        else:  #
            high = mid - 1
    return -1

    #     if arr[mid] >= value:
    #         high = mid - 1
    #     else:
    #         low = mid + 1
    #
    # if low < n and arr[low] == value:
    #     print('查找成功,它的索引为' + str(low))
    #     print("它的值为:")
    #     return value
    # else:
    #     return -1


# 二分查找变形 2.查找第最后一个值等于给定值的元素
def bin_research2(arr, n, value):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        elif mid == (n - 1) or arr[mid + 1] != value:  # 。如果 a[mid] 这个元素已经是数组中的最后一个元素了，那它肯定是我们要找的
            print('查找成功,它的索引为' + str(mid))
            print("它的值为:")
            return value  # 如果 a[mid] 的后一个元素 a[mid+1] 不等于 value，那也说明a[mid] 就是我们要找的最后一个值等于给定值的元素。
        else:
            low = mid + 1
    return -1


# 二分查找变形 3.查找第一个大于等于给定值的元素
def bin_research3(arr, n, value):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] >= value:
            if mid == 0 or arr[mid - 1] < value:  # 看下a[mid]是否为我们么你要找的
                print('查找成功,它的索引为' + str(mid))
                print("它的值为:")
                return value
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


# 二分查找变形 1.查找第一个值小于等于给定值的元素
def bin_research4(arr, n, value):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] <= value:
            if mid == 0 or arr[mid + 1] > value:  # # 看下a[mid]是否为我们么你要找的
                print('查找成功,它的索引为' + str(mid))
                print("它的值为:")
                return value
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1


# 算法测试
def test():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 32]
    n = len(arr)
    print(bin_research(arr, n, 19))
    print(bin_research2(arr, n, 6))
    print(bin_research1(arr, n, 15))
    print(bin_research2(arr, n, 15))
    print(bin_research3(arr, n, 15))
    print(bin_research4(arr, n, 15))


if __name__ == '__main__':
    test()

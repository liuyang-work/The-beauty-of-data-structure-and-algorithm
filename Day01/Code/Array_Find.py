# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm
@File    ：Array_Find.py
@IDE     ：PyCharm
@Author  ：LiuYang
@Date    ：2021/7/22 14:14
"""


# 在数组a中，查找key，返回key所在的位置，其中n表示数组的长度
def find(a, n, key):
    if not a or n <= 0:  # 如果数组为空或者n<=0,说明数组中没有数据，就不用 while 循环比较了
        return -1
    i = 0
    while i < n:  # 这里有两个比较操作：i<n 和 a[i]==key.
        if a[i] == key:
            return i
        i += 1
    return -1


a1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(find(a1, len(a1), 5))


# 列表的三种判空方法
list1 = []
if len(list) == 0:                  # 判断列表长度为0
    print('list is empty')

list2 = []
if not list:                        # 直接逻辑判段
    print('list is empty')


EmptyList = []
list3 = []
if list3 == EmptyList:              # 与空列表对比判断
    print('list is empty')


# 在数组a中，查找key，返回key所在的位置，其中n表示数组的长度
def find(a, n, key):
    if not a or n <= 0:  # 如果数组为空或者n<=0,说明数组中没有数据，就不用 while 循环比较了
        return -1
    # 这里因为要将 a[n-1] 的值替换成 key，所以要特殊处理这个值

    if a[n - 1] == key:
        return n-1

    tmp = a[n - 1]
    a[n-1] = key

    i = 0
    while a[i] != key:
        i += 1
    a[n-1] = tmp

    if i == n-1:
        return -1
    else:
        return i

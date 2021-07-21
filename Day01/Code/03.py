"""
求 1,2,3…n 的累加和
"""


def cal(n):
    sum_int = 0
    for i in range(n+1):       # 范围是 0~n
        sum_int += i           # 复杂度是 O(n)

    return sum_int


print(cal(100))


def cal1(n):
    sum_int1 = 0
    for i in range(n+1):               # 范围是 0~n
        for j in range(1, n + 1):      # 范围是 1~n
            sum_int1 += (i * j)        # 复杂度是 O(n^2)


def cal2(n):
    sum_1 = 0
    for p in range(1, 100):
        sum_1 += p

    sum_2 = 0
    for q in range(1, n):              # 循环n次
        sum_2 += q

    sum_3 = 0
    for i in range(1, n+1):            # 循环n^2次
        for j in range(1, n+1):
            sum_3 += (i*j)

    return sum_1 + sum_2 + sum_3        # 复杂度 O(n^2)


def cal3(n):
    ret = 0
    for i in range(1, n):               # 循环n次
        ret += f(i)                     # 调用f(i) ,f(i)循环n次，复杂度为O(n^2)


def f(n):
    sum_4 = 0
    for i in range(1, n):
        sum_4 += i
    return sum_4


def find(array1, n, x):                  # 在数组中搜索一个数，未找到返回-1
    if array1 is None:
        array1 = []
    pos = -1
    for i in range(n):                  # 复杂度为O(n)
        if array1[i] == x:
            pos = i
            break
    return pos


array = []
length = 10


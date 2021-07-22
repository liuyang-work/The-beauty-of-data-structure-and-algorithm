# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：MyArray.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/7/22 15:54 
"""
from typing import Optional


class MyArray(object):
    def __init__(self, capacity: int):
        """数组类初始化方法"""
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:     # 获取私有属性
        return self._data[position]

    def __setitem__(self, index: int, value: object):   # 设置私有属性
        self._data[index] = value

    def __len__(self) -> int:                           # 获取数组长度
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:               # 按照索引查找元素
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:               # 删除某个元素
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> Optional[bool]:     # 插入元素
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def print_all(self):                                   # 输出数组
        for item in self:
            print(item)


def test_main():
    array = MyArray(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False                # 进行断言
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_main()

# -*- coding: UTF-8 -*-
"""
@Project ：The-beauty-of-data-structure-and-algorithm 
@File    ：Binary_tree.py
@IDE     ：PyCharm 
@Author  ：LiuYang
@Date    ：2021/8/13 10:59 
"""
from typing import TypeVar, Generic, Generator, Optional

"""
    二叉树的前序遍历，中序遍历，后序遍历：
        前序遍历：父节点->左节点->右节点
        中序遍历：左节点->父节点->右节点
        后序遍历：左节点->右节点->父节点
"""

T = TypeVar("T")  # 类型自定义


class TreeNode(Generic[T]):  # 节点定义
    def __init__(self, value: T):
        self.val = value
        self.left = None
        self.right = None


# 前序遍历
def pre_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield root.val
        yield from pre_order(root.left)
        yield from pre_order(root.right)


# 中序遍历
def in_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)


# 后序遍历
def post_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.val


if __name__ == "__main__":
    singer = TreeNode("Taylor Swift")

    genre_country = TreeNode("Country")
    genre_pop = TreeNode("Pop")

    album_fearless = TreeNode("Fearless")
    album_red = TreeNode("Red")
    album_1989 = TreeNode("1989")
    album_reputation = TreeNode("Reputation")

    song_ls = TreeNode("Love Story")
    song_wh = TreeNode("White Horse")
    song_wanegbt = TreeNode("We Are Never Ever Getting Back Together")
    song_ikywt = TreeNode("I Knew You Were Trouble")
    song_sio = TreeNode("Shake It Off")
    song_bb = TreeNode("Bad Blood")
    song_lwymmd = TreeNode("Look What You Made Me Do")
    song_g = TreeNode("Gorgeous")

    singer.left, singer.right = genre_country, genre_pop
    genre_country.left, genre_country.right = album_fearless, album_red
    genre_pop.left, genre_pop.right = album_1989, album_reputation
    album_fearless.left, album_fearless.right = song_ls, song_wh
    album_red.left, album_red.right = song_wanegbt, song_ikywt
    album_1989.left, album_1989.right = song_sio, song_bb
    album_reputation.left, album_reputation.right = song_lwymmd, song_g

    print(list(pre_order(singer)))
    print(list(in_order(singer)))
    print(list(post_order(singer)))

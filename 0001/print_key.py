# -*- coding:UTF-8 -*-
# 第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
import string


def print_key1(length):
    str = ''
    seq = string.ascii_letters + string.digits
    for i in range(length):
        str += random.choice(seq)
    return str


def print_key2(length):
    seq = string.ascii_letters + string.digits
    str = random.sample(seq, length)
    key = ''
    for i in str:
        key += i
    return key


if __name__ == '__main__':
    key1 = print_key1(10)
    print(key1)

    key2 = print_key2(10)
    print(key2)

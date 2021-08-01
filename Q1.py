# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:53:12 2021

@author: miiya
"""

# 入力された数字の形式の暗号を文字列に解読する
def decoder(input_number):
    return chr(int(input_number) + 64)


# 入力された数字の形式の暗号を二桁ごとに区切ってリストに格納する
def formatter(input_number):
    input_list =[]
    while input_number > 0:
        input_list.append(str(input_number%100).zfill(2))
        input_number //= 100
    input_list.reverse()
    return input_list


# 解答する関数
def solver(input_number):
    input_number = formatter(input_number)
    return "".join([decoder(n) for n in input_number])


if __name__ == '__main__':
    # 第1問
    input_number = 23011819  # 今回の問題
    answer = solver(input_number)
    print(answer)
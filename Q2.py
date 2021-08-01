# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:49:48 2021

@author: miiya
"""

import Q1


# mを求める関数
def calc_m(p, q, e):
    flag = True
    m = 0
    while flag:
        m+=1
        flag = ((p-1)*(q-1)*m % e) - (e-1)
    return m


# 秘密鍵dを求める関数
def calc_d(p, q, e, m):
    return (m*(p-1)*(q-1)+1)//e


# Mを求める関数
def calc_M(c, p, q, d):
    n = p*q
    return c**d%n


# (p, q, e)の3つの鍵から暗号を復号する関数
def decrypt(encrypt_text, key):
    c = encrypt_text
    p, q, e = key
    
    m = calc_m(p, q, e)
    print("m: ", m)
    
    d = calc_d(p, q, e, m)
    print("d: ", d)
    
    M = calc_M(c, p, q, d)
    print("M: ", M)
    
    return M
    

if __name__ == '__main__':
    # 第2問
    c = 904  # 暗号文
    
    # 公開鍵
    p = 37
    q = 71
    e = 79
    
    # 暗号文の解読
    Message = decrypt(c, (p, q, e))
    answer = Q1.solver(Message)
    print(answer)

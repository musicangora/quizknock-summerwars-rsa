# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:54:28 2021

@author: miiya
"""

# 試し割り法
def prime_factorize(n):
    a = []
    while n%2==0:  # 最初に偶数を排除
        a.append(2)
        n //= 2
    f = 3
    while f*f <= n:
        if n%f==0:
            a.append(f)
            n//=f
        else:
            f+=2
    if n!=1:
        a.append(n)
    return a


if __name__ == '__main__':
    # 第3問
    pq = 177773
    
    
    p, q = prime_factorize(pq)
    print("p: %d, q: %d"%(p, q))
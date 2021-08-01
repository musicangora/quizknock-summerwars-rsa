# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 17:27:19 2021

@author: miiya
"""

import Q1, Q2, Q3


if __name__ == '__main__':
    # 暗号文
    c = 904
    
    # 公開鍵
    N = 2627
    E = 79
    
    
    # Nからp, qを求める
    p, q = Q3.prime_factorize(N)
    
    # 復号化
    message = Q2.decrypt(c, (p, q, E))
    
    # デコード
    answer = Q1.solver(message)
    
    print(answer)
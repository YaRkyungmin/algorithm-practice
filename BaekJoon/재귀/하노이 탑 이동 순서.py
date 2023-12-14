"""
author: kyungmin
date: 23.12.13
title: 하노이 탑 이동 순서
time: 30분
"""

import sys
input = sys.stdin.readline

input = int(input().rstrip())
def hanoi(a, b, c, n):
    if n == 1:
        print(a, c)
        return
    if n % 2 == 0:
        hanoi(a, c, b, n - 1)
    else:
        hanoi(b, a, c, n - 1)
    print(a, c)
hanoi(1, 2, 3, input)
    
# # 2 ^ n - 1

# ######## n = 1
# 1 3
# ######### n = 2
# 1 2
# 1 3
# 2 3
# ######### n = 3
# 1 3
# 1 2
# 3 2
# 1 3
# 2 1
# 2 3
# 1 3
# ######### n = 4
# 1 2
# 1 3
# 2 3
# 1 2
# 3 1
# 3 2
# 1 2
# 1 3
# 2 3
# 2 1
# 3 1
# 2 3
# 1 2
# 1 3
# 2 3
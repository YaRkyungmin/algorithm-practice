"""
author: kyungmin
date: 24.2.15
title: 돌 게임
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

print("CY" if N % 2 == 0 else "SK")
        

# win = [-1]*10001

# win[1] = 1 #SK
# win[2] = 0 #CY
# win[3] = 1 #SK

# for i in range(4,n+1):
#     if win[i-1] == 1 or win[i-3] == 1:
#         win[i] = 0
#     else:
#         win[i] = 1

# if win[n]==1:
#     print('SK')
# else:
#     print('CY')
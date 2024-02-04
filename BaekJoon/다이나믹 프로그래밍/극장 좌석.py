"""
author: kyungmin
date: 24.2.4
title: 극장 좌석
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
pin = [int(input().rstrip()) for _ in range(M)]
pin.append(N + 1)
result = 1

dp = [1, 1] + [0 for _ in range(N - 1)]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

c = 0

for i in pin:
    if (i - c - 1) != 0:
        result *= dp[(i - c - 1)]
    c = i
    
print(result)



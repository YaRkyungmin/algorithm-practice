"""
author: kyungmin
date: 24.2.11
title: 제곱수의 합
time: 30분
"""
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize

N = int(input().rstrip())
dp = [0, 1] + [MAX_INT for _ in range(1, N)]

for i in range(1, N + 1):
    if i**(1/2) - int(i**(1/2)) == 0:
        dp[i] = 1
        continue
    for j in range(int(i/2), i):
        dp[i] = min(dp[j] + dp[i - j], dp[i])

print(dp[N])
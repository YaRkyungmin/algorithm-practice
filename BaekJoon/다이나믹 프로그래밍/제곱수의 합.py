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

for i in range(2, N + 1):
    for j in range(1, i + 1):
        s = j ** 2
        if s > i :
            break
        if dp[i] > dp[i - s] + 1:
            dp[i] = dp[i - s] + 1

print(dp[N])
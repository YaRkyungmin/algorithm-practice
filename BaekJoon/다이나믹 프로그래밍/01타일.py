"""
author: kyungmin
date: 24.2.9
title: 01타일
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [1, 1] + [0 for _ in range(N - 1)]

for i in range(2, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N])

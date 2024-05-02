"""
author: kyungmin
date: 23.08.31 & 24.05.02
title: 2×n 타일링
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [1, 1] + [0 for _ in range(N - 1)]
for i in range(2, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[N])

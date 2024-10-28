"""
author: kyungmin
date: 24.10.28
title: 합분해
time: 30분
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

dp = [[1] * (N + 1) for _ in range(K)]

for k in range(1, K):
    for n in range(1, N + 1):
        dp[k][n] = dp[k][n - 1] + dp[k - 1][n]

print(dp[K - 1][N] % 1000000000)
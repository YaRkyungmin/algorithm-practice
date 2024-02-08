"""
author: kyungmin
date: 24.2.8
title: 동전 1
time: 30분
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1
for c in coins:
    for i in range(c, k + 1):
        dp[i] += dp[i - c]

print(dp[k])

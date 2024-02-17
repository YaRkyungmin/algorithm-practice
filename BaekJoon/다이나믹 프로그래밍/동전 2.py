"""
author: kyungmin
date: 24.2.17
title: 동전 2
time: 30분
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(n)]
coins.sort()
dp = [10001 for _ in range(k + 1)]
dp[0] = 0

for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0:
            dp[i] = min(dp[i - coin] + 1, dp[i])

print(-1 if dp[k] == 10001 else dp[k])
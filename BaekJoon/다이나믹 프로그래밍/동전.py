"""
author: kyungmin
date: 24.2.12
title: 동전 
time: 30분
"""
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    coins = list(map(int, input().rstrip().split()))
    M = int(input().rstrip())
    dp = [1] + [0 for _ in range(M)]

    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] += dp[i - coin]
    print(dp[M])
"""
author: kyungmin
date: 24.2.6
title: 스티커
time: 30분
"""
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    numbers = [[0] + list(map(int, input().rstrip().split())) for _ in range(2)]
    
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]
    dp[0][1] = numbers[0][1]
    dp[1][1] = numbers[1][1]

    for i in range(2, n + 1):
        dp[0][i] = max(dp[1][i - 1], dp[0][i - 2], dp[1][i - 2]) + numbers[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2], dp[1][i - 2]) + numbers[1][i]
    
    print(max(dp[0][n], dp[1][n]))

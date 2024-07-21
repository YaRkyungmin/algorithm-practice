"""
author: kyungmin
date: 24.7.21
title: 계단 오르기
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = [int(input().rstrip()) for _ in range(N)]
dp = [0 for _ in range(N + 1)]
dp[1] = numbers[0]
if N > 1:
    dp[2] = numbers[1] + numbers[0]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + numbers[i - 1], dp[i - 3] + numbers[i - 2] + numbers[i - 1])
    
print(dp[N])
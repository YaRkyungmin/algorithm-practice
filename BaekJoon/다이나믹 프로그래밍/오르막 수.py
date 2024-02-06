"""
author: kyungmin
date: 24.2.7
title: 오르막 수
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [1 for _ in range(10)]

for _ in range(N - 1):
    for i in range(10):
        dp[i] = sum(dp[i:])

print(sum(dp) % 10007)


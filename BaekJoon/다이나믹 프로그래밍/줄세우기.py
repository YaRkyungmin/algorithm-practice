"""
author: kyungmin
date: 24.09.23
title: 줄세우기
time: 30분
"""
import sys
input = sys.stdin.readline


N = int(input().rstrip())
numbers = [int(input().rstrip()) for _ in range(N)]
dp = [1 for _ in range(N)]
max_count = 1
for i in range(1, N):
    m = 0
    for x in range(0, i):
        if numbers[i] > numbers[x]:
            m = max(m, dp[x])
    dp[i] += m
    max_count = max(max_count, dp[i])
print(N - max_count)
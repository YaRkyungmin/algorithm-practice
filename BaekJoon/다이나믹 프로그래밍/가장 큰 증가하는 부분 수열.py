"""
author: kyungmin
date: 24.1.25
title: 가장 큰 증가하는 부분 수열
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
dp = [0 for _ in range(N)]
result = 0
for i in range(N):
    for x in range(i - 1, -1, -1):
        if numbers[x] < numbers[i]:
            dp[i] = max(dp[x], dp[i])
    dp[i] += numbers[i]
    result = max(dp[i], result)
print(result)
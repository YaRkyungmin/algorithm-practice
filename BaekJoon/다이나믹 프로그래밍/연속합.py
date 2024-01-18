"""
author: kyungmin
date: 24.1.19
title: 연속합
time: 30분
"""
import sys
input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

dp = [0 for _ in range(n)]
dp[0] = numbers[0]
max_result = dp[0]
if n > 1:
    for x in range(1, n):
        if dp[x - 1] > 0:
            dp[x] = numbers[x] + dp[x - 1]
        else:
            dp[x] = numbers[x]
        
        max_result = max(dp[x], max_result)

print(max_result)
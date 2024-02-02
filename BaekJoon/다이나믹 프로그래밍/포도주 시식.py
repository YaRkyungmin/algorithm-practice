"""
author: kyungmin
date: 24.2.2
title: 포도주 시식
time: 30분
"""
import sys
input = sys.stdin.readline

n = int(input().rstrip())
juice = []
for _ in range(n):
    juice.append(int(input().rstrip()))

dp = [0 for _ in range(n)]
dp[0] = juice[0]

if n > 1:
    dp[1] = juice[0] + juice[1]

if n > 2:
    dp[2] = max(juice[0] + juice[1], juice[0] + juice[2], juice[1] + juice[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + juice[i], dp[i - 1], dp[i - 3] + juice[i - 1] + juice[i])

print(dp[n - 1])
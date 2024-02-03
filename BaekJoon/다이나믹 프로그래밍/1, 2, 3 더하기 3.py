"""
author: kyungmin
date: 24.2.3
title: 1, 2, 3 더하기 3
time: 30분
"""

import sys
input = sys.stdin.readline

T = int(input().rstrip())
arr = []
max_num = 0

for _ in range(T):
    n = int(input().rstrip())
    max_num = max(n, max_num)
    arr.append(n)

dp = [0, 0, 1] + [0 for _ in range(max_num)]

for i in range(3, max_num + 3):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009

for i in arr:
    print(dp[i + 2])
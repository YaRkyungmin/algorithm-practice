"""
author: kyungmin
date: 23.08.31
title: 2×n 타일링
time: 30분
"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0] * (N + 1)

dp[0] = 1
dp[1] = 1


for i in range(2, N + 1):
    if i == 2:
        dp[2] = 2
    else:
        dp[i] = 2 * dp[i-1] - dp[i-3]
print(dp[N] % 10007)

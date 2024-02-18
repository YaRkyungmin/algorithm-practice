"""
author: kyungmin
date: 24.2.18
title: 타일 채우기
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [0 for _ in range(N + 1)]
dp[0] = 1
if N >= 2:
    dp[2] = 3
    for i in range(4, N + 1, 2):
        if i >= 6:
            dp[i] = dp[i - 2] * 3 + dp[i - 4] * 2 + dp[i - 6] * 2
        else:
            dp[i] = dp[i - 2] * 3 + dp[i - 4] * 2
print(dp[N])
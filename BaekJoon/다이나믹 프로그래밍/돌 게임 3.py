"""
author: kyungmin
date: 24.2.20
title: 돌 게임 3
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [0, 1, 0, 1, 1] + [0 for _ in range(N - 4)]

for i in range(5, N + 1):
    if dp[i - 1] == 0\
    or dp[i - 3] == 0\
    or dp[i - 4] == 0:
        dp[i] = 1

print("SK" if dp[N] == 1 else "CY")

# print('CY' if int(input())%7 in (0,2) else 'SK')

"""
author: kyungmin
date: 24.1.31
title: 1로 만들기 2
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0 for _ in range(N + 1)]
history = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    history[i] = i - 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        history[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        history[i] = i // 2
    
print(dp[N])
dist = []
p = N
while p != 0:
    dist.append(p)
    p = history[p]
print(*dist)
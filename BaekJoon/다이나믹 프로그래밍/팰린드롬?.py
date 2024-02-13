"""
author: kyungmin
date: 24.2.14
title: 팰린드롬?
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
questions = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
dp = [[0]* N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(1, N):
    dp[i - 1][i] = 1 if questions[i-1] == questions[i] else 0

for i in range(2, N):
    for z in range(0, N - i):
        if questions[z + i] == questions[z]\
        and dp[z + 1][z + i - 1] == 1:
            dp[z][z + i] = 1

for _ in range(M):
    S, E = map(int, input().rstrip().split())
    print(dp[S - 1][E - 1])
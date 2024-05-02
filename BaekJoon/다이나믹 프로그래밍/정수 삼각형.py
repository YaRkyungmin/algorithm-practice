"""
author: kyungmin
date: 24.5.2
title: 정수 삼각형
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
tree = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0] * i for i in range(1, N + 1)]
dp[0][0] = tree[0][0]
result = 0

for i in range(1, N):
    for x in range(i + 1):
        if x == 0:
            dp[i][x] = dp[i - 1][x] + tree[i][x]
        elif x == i:
            dp[i][x] = dp[i - 1][x - 1] + tree[i][x]
        else:
            dp[i][x] = max(dp[i - 1][x - 1], dp[i - 1][x]) + tree[i][x]

for i in range(N):
    result = max(dp[N - 1][i], result)

print(result)
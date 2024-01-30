"""
author: kyungmin
date: 24.1.30
title: RGB거리
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

rgb = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0, 0 , 0] for _ in range(N)]
dp[0] = rgb[0]
for y in range(1, N):
    dp[y][0] = min(dp[y - 1][1] + rgb[y][0], dp[y - 1][2] + rgb[y][0])
    dp[y][1] = min(dp[y - 1][0] + rgb[y][1], dp[y - 1][2] + rgb[y][1])
    dp[y][2] = min(dp[y - 1][0] + rgb[y][2], dp[y - 1][1] + rgb[y][2])

print(min(dp[N - 1]))
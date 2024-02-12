"""
author: kyungmin
date: 24.2.13
title: 가장 큰 정사각형
time: 30분
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
rectangle = [list(map(int, input().rstrip())) for _ in range(n)]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
result = 0

for y in range(1, n + 1):
    for x in range(1, m + 1):
        if rectangle[y - 1][x - 1] == 1:
            side = min(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1]) # 변의 길이만 구하면 됨
            dp[y][x] = side + 1
            result = max(side + 1, result)

print(result * result)


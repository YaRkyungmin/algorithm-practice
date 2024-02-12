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
dx = [-1,-1]
dy = [0,-1]
result = 0

for y in range(1, n + 1):
    for x in range(1, m + 1):
        if rectangle[y - 1][x - 1] == 1:
            side = dp[y - 1][x]
            for i in range(2):
                px = x + dx[i]
                py = y + dy[i]
                side = min(dp[py][px], side)
            p_result = 0
            if side == 0:
                p_result = 1
            else:
                p_result = int((side ** 0.5 + 1) ** 2)
            
            result = max(p_result, result)
            dp[y][x] = p_result

print(result)


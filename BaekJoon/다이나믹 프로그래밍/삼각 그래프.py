"""
author: kyungmin
date: 24.1.25
title: 삼각 그래프
time: 30분
"""
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize
k = 1
while True:
    N = int(input().rstrip())
    if N == 0:
        break
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]


    dp = [[0, 0, 0] for _ in range(N)]
    dp[0][0] = MAX_INT
    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][1] + graph[0][2]

    dx = [-1, -1, 0, 1]
    dy = [0, -1, -1, -1]
    for y in range(1, N):
        for x in range(3):
            m_value = MAX_INT
            for i in range(4):
                px = x + dx[i]
                py = y + dy[i]
                if 0 <= px < 3:
                    m_value = min(dp[py][px] + graph[y][x], m_value) 
            dp[y][x] = m_value

    print(f"{k}. {dp[N - 1][1]}")
    k += 1

    
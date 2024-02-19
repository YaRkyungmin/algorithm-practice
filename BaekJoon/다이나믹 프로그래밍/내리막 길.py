"""
author: kyungmin
date: 24.2.19
title: 내리막 길
time: 30분
"""
## DFS와 DP 를 이용한 재귀 풀이도 무조건 풀어보자!
import sys
input = sys.stdin.readline
import heapq

M, N = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(M)]

heap = [(-graph[0][0], 0, 0)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

dp = [[0 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1

while heap:
    h, x, y = heapq.heappop(heap)
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        
        if 0 <= px < N\
        and 0 <= py < M\
        and graph[py][px] < -h:
            if dp[py][px] != 0:
                dp[py][px] += dp[y][x]
            else:
                dp[py][px] += dp[y][x]
                heapq.heappush(heap,(-graph[py][px], px, py))

print(dp[M - 1][N - 1])
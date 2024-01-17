"""
author: kyungmin
date: 24.1.18
title: 알고스팟
time: 30분
"""
import sys
import heapq
MAX_INT = sys.maxsize
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
graph = []
for _ in range(N):
    row = list(map(int, input().rstrip()))
    graph.append(row)

for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            graph[y][x] = 2
        else:
            graph[y][x] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dist = [[MAX_INT for _ in range(M)] for _ in range(N)]
dist[0][0] = 0
heap = [(0, 0, 0, 0)]
dis_count = 0

while heap:
    c, x, y, distance_count = heapq.heappop(heap)
    if dist[y][x] < c:
        continue
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        if 0 <= px < M\
        and 0 <= py < N\
        and dist[py][px] > (c + graph[py][px]):
            cost = c + graph[py][px]
            heapq.heappush(heap, (cost, px, py, distance_count + 1))
            dist[py][px] = c + cost
            if py == N - 1 and px == M - 1:
                dis_count = distance_count + 1

print((dist[N - 1][M - 1]) - dis_count)
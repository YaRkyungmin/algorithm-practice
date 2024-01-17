"""
author: kyungmin
date: 24.1.17
title: 최소비용 구하기
time: 30분
"""
import sys
import heapq
INT_MAX = sys.maxsize
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
town = [[] for _ in range(N + 1)]

for _ in range(M):
    dv, av, edge = map(int, input().rstrip().split())
    town[dv].append((av, edge))

A, B = map(int, input().rstrip().split())
town[B] = []
dist = [INT_MAX for _ in range(N + 1)]
heap = []
dist[A] = 0
heapq.heappush(heap, (0, A))
visit = [False for _ in range(N + 1)]
visit[A] = True
while heap:
    c, v = heapq.heappop(heap)
    #### 이 영역이 무조건 필요!
    if c > dist[v]:
        continue
    ####
    for pv, pc in town[v]:
        if dist[pv] > pc + c:
            dist[pv] = pc + c
            heapq.heappush(heap, (pc + c, pv))

print(dist[B])



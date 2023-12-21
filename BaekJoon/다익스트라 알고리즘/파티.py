"""
author: kyungmin
date: 23.12.21
title: 파티
time: 30분
"""
import sys
input = sys.stdin.readline
import heapq
MAX_INT = sys.maxsize

N, M, X = map(int, input().rstrip().split())
# vertices, edges, target point
village = [[] for _ in range(N + 1)]
village2 = [[] for _ in range(N + 1)]
for _ in range(M):
    dv, av, weight = map(int, input().rstrip().split())
    village[dv].append((av, weight))
    village2[av].append((dv, weight))
def min_dictance(start, graph):
    global N
    heap = []
    D = [MAX_INT for _ in range(N + 1)]
    D[start] = 0
    D[0] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, vertex = heapq.heappop(heap)
        for (dv, dw) in graph[vertex]:
            if dw + weight < D[dv]:
                D[dv] = dw + weight
                heapq.heappush(heap, (dw + weight, dv))
    return D
# 왕복 저장
vil1 = min_dictance(X, village)
vil2 = min_dictance(X, village2)
print(max([vil1[i] + vil2[i] for i in range(N + 1)]))
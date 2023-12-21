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
for _ in range(M):
    dv, av, weight = map(int, input().rstrip().split())
    village[dv].append((av, weight))
def min_dictance(start, end):
    global N
    heap = []
    D = [MAX_INT for _ in range(N + 1)]
    D[start] = 0
    heapq.heappush(heap, (0, start))
    m_d = 0
    while heap:
        weight, vertex = heapq.heappop(heap)
        if weight == D[vertex]:
            for (dv, dw) in village[vertex]:
                if dv != start and dw + weight < D[dv]:
                    D[dv] = dw + weight
                    if dv == end:
                        m_d = dw + weight
                        continue
                    heapq.heappush(heap, (dw + weight, dv))
    return m_d
# 왕복 저장
round_arr = [0 for _ in range(N + 1)]

for x in range(1, N + 1):
    if x == X:
        continue
    round_arr[x] += min_dictance(x, X)

for x in range(1, N + 1):
    if x == X:
        continue
    round_arr[x] += min_dictance(X, x)

print(max(round_arr))
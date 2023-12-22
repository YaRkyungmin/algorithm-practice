"""
author: kyungmin
date: 23.12.21
title: 특정한 최단 경로
time: 30분
"""
import heapq
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize

N, E = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    av, bv, cweight = map(int, input().split())
    graph[av].append((bv, cweight))
    graph[bv].append((av, cweight))
d1, d2 = map(int, input().rstrip().split())
min_distance = 0
signal = False

def djk(n):
    global N, signal
    heap = []
    heapq.heappush(heap, (0, n))
    D = [MAX_INT for _ in range(N + 1)]
    D[n] = 0

    while heap:
        weight, vertex = heapq.heappop(heap)

        for (dv, dw) in graph[vertex]:
            if dw + weight < D[dv]:
                D[dv] = dw + weight
                heapq.heappush(heap, (dw + weight, dv))
    if D[1] == MAX_INT or D[N] == MAX_INT:
        signal = True
    return (D[1], D[N])

def djk2(n, d):
    global N, signal
    heap = []
    heapq.heappush(heap, (0, n))
    D = [MAX_INT for _ in range(N + 1)]
    D[n] = 0

    while heap:
        weight, vertex = heapq.heappop(heap)

        for (dv, dw) in graph[vertex]:
            if dw + weight < D[dv]:
                D[dv] = dw + weight
                heapq.heappush(heap, (dw + weight, dv))
    if D[d] == MAX_INT:
        signal = True
    return D[d]

a1, a2 = djk(d1)
b1, b2 = djk(d2)
min_distance += djk2(d1, d2)
min_distance += a1 + b2 if a1 + b2 < a2 + b1 else a2 + b1

print(-1 if signal else min_distance)
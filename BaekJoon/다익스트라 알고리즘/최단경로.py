"""
author: kyungmin
date: 23.12.19
title: 최단경로
time: 30분
"""
import sys
input = sys.stdin.readline
import heapq
MAX_INT = sys.maxsize
V, E = map(int, input().rstrip().split())
s_node = int(input().rstrip())
graph = [[] for _ in range(V + 1)]
D = [MAX_INT for _ in range(V + 1)]
D[s_node] = 0

for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))
heap = []

heapq.heappush(heap, (0, s_node))
while heap:
    weight, vertex = heapq.heappop(heap)

    if weight == D[vertex]:
        for (d_vertex, d_weight) in graph[vertex]:
            if D[d_vertex] > weight + d_weight:
                D[d_vertex] = weight + d_weight
                heapq.heappush(heap, (weight + d_weight, d_vertex))
            
for i in range(1, V + 1):
    if D[i] == MAX_INT:
        print("INF")
    else:
        print(D[i])
"""
author: kyungmin
date: 23.12.20
title: 최소비용 구하기 2
time: 30분
"""
import sys
import heapq
input = sys.stdin.readline
MAX_INT = sys.maxsize

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    dv, av, weight = map(int, input().rstrip().split())
    graph[dv].append((av, weight))
d_node, a_node = map(int, input().rstrip().split())
# 최소 비용
# 포함된 도시 갯수 (출발, 도착 포함)
# 최소비용을 가지도록 경로를 방문하는 도시 순서대로 출력

heap = []
heapq.heappush(heap, (0, d_node, [d_node]))
D = [MAX_INT for _ in range(n + 1)]
D[d_node] = 0
answer = []
while heap:
    weight, vertax, visit = heapq.heappop(heap)
    b_siganl = False
    if vertax == a_node:
        continue
    if D[vertax] == weight:
        for (p_vertax, p_weight) in graph[vertax]:
            if p_weight + weight < D[p_vertax]:
                n_visit = visit.copy()
                n_visit.append(p_vertax)
                heapq.heappush(heap, (p_weight + weight, p_vertax, n_visit))
                D[p_vertax] = p_weight + weight
                if p_vertax == a_node:
                    answer = n_visit

print(D[a_node])
print(len(answer))
print(*answer)

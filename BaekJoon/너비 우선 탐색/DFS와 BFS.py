"""
author: kyungmin
date: 23.06.27
title: DFS와 BFS
time: 30분
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

for _ in range(M):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)
for i in range(N+1):
    graph[i] = sorted(graph[i])

dfs_check_visit = [False] * (N + 1)
dfs_visit = []
def dfs(start):
    if dfs_check_visit[start] == False:
        dfs_check_visit[start] = True
        dfs_visit.append(start)
        for i in graph[start]:
            dfs(i)
            
queue = deque()
bfs_check_visit = [False] * (N + 1)
bfs_visit = []
def bfs(start):
    queue.append(start)
    while queue:
        node = queue.popleft()
        if bfs_check_visit[node] == False:
            bfs_check_visit[node] = True
            bfs_visit.append(node)
            queue.extend(graph[node])
dfs(V)
bfs(V)
print(*dfs_visit)
print(*bfs_visit)
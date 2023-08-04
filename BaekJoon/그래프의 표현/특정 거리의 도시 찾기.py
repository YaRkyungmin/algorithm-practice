"""
author: kyungmin
date: 23.08.07
title: 특정 거리의 도시 찾기
time: 30분
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append([B, 0])

bfs_queue = deque()
visited = [False] * (N + 1)
cnt = 0
result = []
def BFS(node):
    global cnt, K
    bfs_queue.append(node)
    visited[node[0]] = True
    while bfs_queue:
        pop_node = bfs_queue.popleft()
        if visited[pop_node[0]] == False:
            visited[pop_node[0]] = True
            if K == pop_node[1]:
                result.append(pop_node[0])
                continue
            for i in range(len(graph[pop_node[0]])):
                append_node = graph[pop_node[0]][i][0]
                depth = pop_node[1] + 1
                bfs_queue.append([append_node, depth])

BFS([X, 0])

if result:
    print(*result, sep="\n")
else:
    print(-1)

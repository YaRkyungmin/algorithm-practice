"""
author: kyungmin
date: 23.06.22
title: 연결 요소의 개수
time: 30분
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

visited = [True] * (N + 1)

cnt = 0

def dfs_recusive(start):
    if visited[start]:
        visited[start] = False
        for element in graph[start]:
            dfs_recusive(element)

for i in range(1, N+1):
    if visited[i]:
        dfs_recusive(i)
        cnt += 1
print(cnt)
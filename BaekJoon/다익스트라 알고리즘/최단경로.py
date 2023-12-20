"""
author: kyungmin
date: 23.12.19
title: 최단경로
time: 30분
"""
import sys
input = sys.stdin.readline
from collections import deque

V, E = map(int, input().rstrip().split())
s_node = int(input().rstrip())
graph = [[] for _ in range(V + 1)]
D = [0 for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))
queue = deque()

queue.append((s_node, 0))
while queue:
    p_node, length = queue.popleft()
    t_dic = dict()
    if graph[p_node]:
        for (dn, dlength) in graph[p_node]:
            if dn in t_dic:
                t_dic[dn] = min(t_dic[dn], dlength)
            else:
                t_dic[dn] = dlength
    for node, dlength in t_dic.items():
        if D[node] == 0:
            D[node] = length + dlength
        else:
            D[node] = min(D[node], length + dlength)

        queue.append((node, D[node]))

for i in range(1, V + 1):
    if i != s_node and D[i] == 0:
        print("INF")
    else:
        print(D[i])

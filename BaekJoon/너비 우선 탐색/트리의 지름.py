"""
author: kyungmin
date: 23.06.29
title: 트리의 지름
time: 30분
"""
import sys
from collections import deque
input = sys.stdin.readline

V = int(input().rstrip())

graph = [[] for _ in range(V + 1)]

for node in range(1, V+1):
    node_list = list(map(int, input().split()))
    i = 1
    while node_list[i] != -1:
        graph[node].append((node_list[i],node_list[i + 1]))
        i += 2

queue = deque()
visit = []
depth = 0

def dfs(start):
    queue.append(start)
    while queue:
        node = queue.pop()
        if node[0] not in visit:
            visit.append(node[0])
            depth += node[1]
            queue.append(graph[node][-1])


# def find_max_depth(node_list):
#     max = node_list[0]
#     for i in range(len(node_list)):
#         if max[1] < 
"""
author: kyungmin
date: 23.08.08
title: 효율적인 해킹
time: 30분
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    graph[B].append(A)

global_visit_list = [False] * (N + 1)

# def DFS(node):
#     visit = [False] * (N + 1)
#     visit_count = 0
#     stack = []
#     stack.append(node)
#     while stack:
#         pop_node = stack.pop()
#         if visit[pop_node] == False:
#             visit_count += 1
#             global_visit_list[pop_node] = True
#             visit[pop_node] = True
#             stack.extend(graph[pop_node])
            
#     return visit_count

def BFS(node):
    visit = [False] * (N + 1)
    visit_count = 0
    stack = deque()
    stack.append(node)
    while stack:
        pop_node = stack.popleft()
        if visit[pop_node] == False:
            visit_count += 1
            global_visit_list[pop_node] = True
            visit[pop_node] = True
            stack.extend(graph[pop_node])
            
    return visit_count

visit_count_list = []
max_visit_count_list = 0

for i in range(1, N+1):
    if global_visit_list[i] == False:
        visit_count = BFS(i)
    
        if max_visit_count_list < visit_count:
            max_visit_count_list = visit_count
            visit_count_list = []
            visit_count_list.append(i)
        elif max_visit_count_list == visit_count:
            visit_count_list.append(i)

print(*visit_count_list, sep= ' ')
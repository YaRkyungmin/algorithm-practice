"""
author: kyungmin
date: 23.08.10
title: 이분 그래프
time: 30분
"""
import sys
from collections import deque
input = sys.stdin.readline

K = int(input().rstrip())

def change(color):
    if color == 0:
        return 1
    else:
        return 0
result_list = []

for _ in range(K):
    V, E = map(int, input().rstrip().split())

    grahp = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().rstrip().split())
        grahp[u].append(v)
        grahp[v].append(u)

    queue = deque()

    color_list = [0 for _ in range(V + 1)]
    visit = [False] * (V + 1)
    
    def BFS(node):
        node_linked_list = grahp[node]
        node_count = len(node_linked_list)

        for i in range(node_count):
            queue.append((node_linked_list[i], color_list[node]))
        
        while queue:
            (pop_node, pop_color) = queue.popleft()
            pop_node_linked_list = grahp[pop_node]
            pop_node_count = len(pop_node_linked_list)
            append_color = change(pop_color)

            for i in range(pop_node_count):
                append_node = pop_node_linked_list[i]

                if visit[append_node] == False:
                    visit[append_node] = True
                    queue.append((append_node, append_color))
                    color_list[append_node] = append_color
                else:
                    if color_list[append_node] != append_color:
                        return 1
        return 0
    
    last_result = 0
    for i in range(1, V+1):
        if last_result == 0:
            if visit[i] == False:
                last_result = BFS(i)
        else:
            break
    
    if last_result == 0:
        result_list.append("YES")
    else:
        result_list.append("NO")

print(*result_list, sep="\n")
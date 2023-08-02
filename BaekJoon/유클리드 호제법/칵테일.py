"""
author: kyungmin
date: 23.07.27
title: 칵테일
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N)]
LCM = 1

def GD(a, b):
    if a % b == 0:
        return b    
    return GD(b, a % b)

visit = [False] * N
dfs_stack = []

def DFS(node):
    dfs_stack.extend(graph[node])
    visit[node] = True
    while dfs_stack:
        pop_node = dfs_stack.pop()
        if visit[pop_node[0]] == False:
            visit[pop_node[0]] = True
            D[pop_node[0]] = D[pop_node[3]]//pop_node[1] * pop_node[2]
            dfs_stack.extend(graph[pop_node[0]])

for _ in range(N-1):
    a, b, p, q = map(int, input().rstrip().split())
    graph[a].append((b, p, q, a))
    graph[b].append((a, q, p, b))

    LCM *= (p * q) // GD(p, q)

D = [0] * N
D[0] = LCM
DFS(0)

MGCD = D[0]

for i in range(N):
    MGCD = GD(MGCD,D[i])

for i in range(N):
    print(D[i]//MGCD, end = ' ')
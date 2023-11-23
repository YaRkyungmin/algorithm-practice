"""
author: kyungmin
date: 23.11.24
title: 그림
time: 30분
"""
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

paper = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    line = list(map(int, input().split()))
    paper.append(line)

visit = [[0] * m for _ in range(n)]

count = 0
max_depth = 0

def dfs():
    global max_depth, count
    one_arr = []
    flag = False
    for y in range(n):
        for x in range(m):
            if paper[y][x] == 1:
                one_arr.append([x,y])
            else:
                continue
    
    for node in one_arr:
        if visit[node[1]][node[0]] == 1:
            continue
        else:
            queue = deque()
            queue.append([node[0], node[1]])
            visit[node[1]][node[0]] = 1
            m_depth = 1

            while queue:
                [x, y] = queue.pop()
                
                for i in range(4):
                    if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n and paper[y + dy[i]][x + dx[i]] == 1 and visit[y + dy[i]][x + dx[i]] == 0:
                        queue.append([x + dx[i], y + dy[i]])
                        visit[y + dy[i]][x + dx[i]] = 1
                        m_depth += 1
                
            max_depth = max(max_depth, m_depth)
            count += 1

dfs()

print(f"{count}\n{max_depth}")
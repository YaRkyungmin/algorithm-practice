"""
author: kyungmin
date: 23.12.03
title: 유기농 배추
time: 30분
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(map):
    visit = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0 
    queue = deque()
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 1 and visit[y][x] == 0:
                queue.append([x, y])
                while queue:
                    nx, ny = queue.popleft()

                    for i in range(4):
                        if 0 <= nx + dx[i] < len(map[0]) and 0 <= ny + dy[i] < len(map) and map[ny + dy[i]][nx + dx[i]] == 1 and visit[ny + dy[i]][nx + dx[i]] == 0:
                            queue.append([nx + dx[i], ny + dy[i]])
                            visit[ny + dy[i]][nx + dx[i]] = 1
                count += 1
    
    return count 

T = int(input().rstrip())

for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        farm[y][x] = 1
    
    print(bfs(farm))
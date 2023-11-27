"""
author: kyungmin
date: 23.11.28
title: 토마토
time: 30분
"""
import sys
import copy
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

box = []
cpl_tos = []
memory = [[[] for _ in range(M)] for _ in range(N)]


for y in range(N):
    row = list(map(int, input().split()))
    for x in range(M):
        if row[x] == 1:
            cpl_tos.append([x, y])
    box.append(row)

def bfs(x, y, day):
    global M, N
    queue = deque()
    queue.append([x, y, day])
    memory[y][x].append(day)
    new_box = copy.deepcopy(box)

    while queue:
        [nx, ny, nday] = queue.popleft()

        if nx - 1 >= 0 and new_box[ny][nx-1] == 0:
            queue.append([nx - 1, ny, nday + 1])
            new_box[ny][nx-1] = 1
            memory[ny][nx-1].append(nday + 1) 
        if nx + 1 < M and new_box[ny][nx +1] == 0:
            queue.append([nx + 1, ny, nday + 1])
            new_box[ny][nx +1] = 1
            memory[ny][nx +1].append(nday + 1) 
        if ny - 1 >= 0 and new_box[ny - 1][nx] == 0:
            queue.append([nx, ny -1, nday + 1])
            new_box[ny - 1][nx] = 1
            memory[ny - 1][nx].append(nday + 1) 
        if ny + 1 < N and new_box[ny + 1][nx] == 0:
            queue.append([nx, ny +1, nday + 1])
            new_box[ny + 1][nx] = 1
            memory[ny + 1][nx].append(nday + 1)

for cpl_to in cpl_tos:
    bfs(cpl_to[0], cpl_to[1], 0)

signal = False
result = 0

for y in range(N):
    for x in range(M):
        if box[y][x] == 0:
            if len(memory[y][x]) == 0:
                signal = True
            else:
                result = max(result, (sum(memory[y][x]) / len(memory[y][x])))

if signal:
    print(-1)
else:
    print(int(result))
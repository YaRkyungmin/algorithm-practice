"""
author: kyungmin
date: 23.11.28
title: 토마토
time: 30분
"""
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

box = []
cpl_tos = []
memory = [[0 for _ in range(M)] for _ in range(N)]
queue = deque()

for y in range(N):
    row = list(map(int, input().split()))
    for x in range(M):
        if row[x] == 1:
            queue.append([x, y, 0])
    box.append(row)

def bfs():
    global M, N

    while queue:
        [nx, ny, nday] = queue.popleft()

        if nx - 1 >= 0 and box[ny][nx-1] == 0:
            queue.append([nx - 1, ny, nday + 1])
            box[ny][nx-1] = 1
            memory[ny][nx-1]= nday + 1
        if nx + 1 < M and box[ny][nx +1] == 0:
            queue.append([nx + 1, ny, nday + 1])
            box[ny][nx +1] = 1
            memory[ny][nx +1] = nday + 1
        if ny - 1 >= 0 and box[ny - 1][nx] == 0:
            queue.append([nx, ny -1, nday + 1])
            box[ny - 1][nx] = 1
            memory[ny - 1][nx] = nday + 1
        if ny + 1 < N and box[ny + 1][nx] == 0:
            queue.append([nx, ny +1, nday + 1])
            box[ny + 1][nx] = 1
            memory[ny + 1][nx] = nday + 1

bfs()

signal = False
result = 0

for y in range(N):
    for x in range(M):
        if box[y][x] == 0:
            signal = True
        else:
            result = max(result, memory[y][x])

if signal:
    print(-1)
else:
    print(int(result))
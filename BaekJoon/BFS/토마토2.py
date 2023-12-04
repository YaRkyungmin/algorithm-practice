"""
author: kyungmin
date: 23.12.04
title: 토마토2
time: 30분
"""

import sys
from collections import deque

M, N, H = map(int, input().rstrip().split())

box = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
visit = [[[0] * M for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
count = 1
queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1 and visit[z][y][x] == 0:
                queue.append([x, y, z])
                visit[z][y][x] = 1
while queue:
    px, py, pz = queue.popleft()
    for i in range(6):
        nx = px + dx[i]
        ny = py + dy[i]
        nz = pz + dz[i]
        if 0 <= nx < M\
        and 0 <= ny < N\
        and 0 <= nz < H\
        and box[nz][ny][nx] == 0\
        and visit[nz][ny][nx] == 0:
            visit[nz][ny][nx] = visit[pz][py][px] + 1
            count = max(count, visit[nz][ny][nx])
            queue.append([nx, ny, nz])

count -= 1
signal = False
        
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0 and visit[z][y][x] == 0:
                signal = True

if signal:
    print(-1)
else:
    print(count)
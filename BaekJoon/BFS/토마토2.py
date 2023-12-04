"""
author: kyungmin
date: 23.12.04
title: 토마토2
time: 30분
"""

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split())

box = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
count = 0
queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                queue.append([x, y, z])
while queue:
    px, py, pz = queue.popleft()
    for i in range(6):
        nx = px + dx[i]
        ny = py + dy[i]
        nz = pz + dz[i]
        if 0 <= nx < M\
        and 0 <= ny < N\
        and 0 <= nz < H\
        and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = box[pz][py][px] + 1 #visit을 사용하지 않음으로써 메모리를 아낄 수 있음
            count = box[pz][py][px]
            queue.append([nx, ny, nz])

signal = False
        
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                signal = True

if signal:
    print(-1)
else:
    print(count)
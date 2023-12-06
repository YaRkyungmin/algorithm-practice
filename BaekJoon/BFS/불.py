"""
author: kyungmin
date: 23.12.06
title: 불
time: 30분
"""
import sys
input = sys.stdin.readline
from collections import deque

tc = int(input().rstrip())
for _ in range(tc):
    w, h = map(int, input().rstrip().split())
    tawor = [list(input().rstrip()) for _ in range(h)]
    tx, ty = [0, 0]
    queue = deque()
    for y in range(h):
        for x in range(w):
            if tawor[y][x] == "@":
                tx = x
                ty = y
            if tawor[y][x] == "*":
                queue.append((x, y))
    
    queue.append((tx, ty))
    tawor[ty][tx] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    signal = False
    while queue:
        nx, ny = queue.popleft()
        if tawor[ny][nx] == "*": # 불일때
            for i in range(4):
                px = nx + dx[i]
                py = ny + dy[i]
                if 0 <= px < w\
                and 0 <= py < h\
                and tawor[py][px] == ".":
                    tawor[py][px] = "*"
                    queue.append((px, py))
        elif tawor[ny][nx] != "#" and tawor[ny][nx] != ".": # 사람일때
            if nx == 0 or nx == (w-1) or ny == 0 or ny == (h-1): # 탈출 가능 할 때
                count = tawor[ny][nx]
                signal = True
                break
            for i in range(4):
                px = nx + dx[i]
                py = ny + dy[i]
                if 0 <= px < w\
                and 0 <= py < h\
                and tawor[py][px] == ".":
                    tawor[py][px] = tawor[ny][nx] + 1
                    queue.append((px, py))
    
    print(count if signal else "IMPOSSIBLE")
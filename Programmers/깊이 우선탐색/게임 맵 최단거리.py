"""
author: kyungmin
date: 23.10.02
title: 게임 맵 최단거리
time: 30분
"""
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0,0))
    result = -1
    while queue:
        nx, ny = queue.popleft()
        if nx == (m - 1) and ny == (n - 1):
            result = maps[ny][nx]
        for i in range(4):
            px = nx + dx[i]
            py = ny + dy[i]
            if 0 <= px < m\
            and 0 <= py < n\
            and maps[py][px] == 1:
                maps[py][px] = maps[ny][nx] + 1
                queue.append((px, py))
    return result
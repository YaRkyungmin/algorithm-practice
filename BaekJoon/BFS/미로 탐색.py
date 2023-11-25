"""
author: kyungmin
date: 23.11.26
title: 미로 탐색
time: 30분
"""

import sys
from collections import deque

N, M = map(int, input().split())

map = []
for _ in range(N):
    row = []
    for i in input():
        row.append(int(i))
    map.append(row)

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
count = 1
queue = deque()
queue.append([0,0,1])
visit = [[0 for _ in range(M)] for _ in range(N)]
visit[0][0] = 1
signal = False
while queue:
    [x, y, depth] = queue.popleft()
    
    for i in range(4):
        if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N and visit[y + dy[i]][x + dx[i]] == 0 and map[y + dy[i]][x + dx[i]] == 1:
            if x + dx[i] == M-1 and y + dy[i] == N-1:
                count = depth + 1
                signal = True
                break
            queue.append([x + dx[i], y + dy[i], depth + 1])
            visit[y + dy[i]][x + dx[i]] = 1
    if signal:
        break
print(count)

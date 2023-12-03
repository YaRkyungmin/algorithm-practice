"""
author: kyungmin
date: 23.12.03
title: 적록색약
time: 30분
"""

from collections import deque

N = int(input())
picture = [list(input()) for _ in range(N)]

visit = [[0] * N for _ in range(N)]
o_count = 0
x_count = 0

dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    c_color = picture[y][x]
    queue.append([x, y])
    visit[y][x] = 1 # 어디서 visit을 처리해주는지가 아주 중요
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            if 0 <= ny + dy[i] < N and 0 <= nx + dx[i] < N and visit[ny + dy[i]][nx + dx[i]] == 0 and picture[ny + dy[i]][nx + dx[i]] == c_color:
                queue.append([nx + dx[i], ny + dy[i]])
                visit[ny + dy[i]][nx + dx[i]] = 1 # visit을 처리해주는 부분을 새로운 길을 찾을 때 바로 해야 다른 노드에서 겹치는 길을 큐에 안담는다.

for y in range(N):
    for x in range(N):
        if visit[y][x] == 1:
            continue
        bfs(x, y)
        o_count += 1

visit = [[0] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if picture[y][x] == "G":
            picture[y][x] = "R"

for y in range(N):
    for x in range(N):
        if visit[y][x] == 1:
            continue
        bfs(x, y)
        x_count += 1

print(o_count, x_count)
"""
author: kyungmin
date: 23.12.03
title: 적록색약
time: 30분
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
picture = []

for _ in range(N):
    row = list(input().rstrip())
    picture.append(row)

visit = [[0 for _ in range(N)] for _ in range(N)]
o_count = 0
x_count = 0

dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]
queue = deque()
for y in range(N):
    for x in range(N):
        if (picture[y][x] == "R" or picture[y][x] == "G") and visit[y][x] == 0:
            sss = set()
            queue.append([x, y])
            while queue:
                nx, ny = queue.popleft()
                sss.add(picture[ny][nx])
                visit[ny][nx] = 1
                for i in range(4):
                    if 0 <= ny + dy[i] < N \
                        and 0 <= nx + dx[i] < N \
                            and visit[ny + dy[i]][nx + dx[i]] == 0 \
                                and (picture[ny + dy[i]][nx + dx[i]] == "R" or picture[ny + dy[i]][nx + dx[i]] == "G"):
                        queue.append([nx + dx[i], ny + dy[i]])
            o_count += len(sss)
            x_count += 1
        elif picture[y][x] == "B" and visit[y][x] == 0:
            queue.append([x, y])
            while queue:
                nx, ny = queue.popleft()
                visit[ny][nx] = 1
                for i in range(4):
                    if 0 <= ny + dy[i] < N \
                        and 0 <= nx + dx[i] < N \
                            and visit[ny + dy[i]][nx + dx[i]] == 0 \
                                and picture[ny + dy[i]][nx + dx[i]] == "B":
                        queue.append([nx + dx[i], ny + dy[i]])
            o_count += 1
            x_count += 1

print(o_count, x_count)
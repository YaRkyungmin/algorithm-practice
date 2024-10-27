"""
author: kyungmin
date: 23.12.07
title: 벽 부수고 이동하기
time: 30분
"""
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
### 3D bfs
# N, M = map(int, input().rstrip().split())
# gmap = [[int(i) for i in input().rstrip()] for _ in range(N)]
# queue = deque()
# visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
# visit[0][0][0] = 1
# queue.append((0, 0, 0))
# count = -1
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# while queue:
#     nx, ny, broken = queue.popleft()

#     if ny == N - 1 and nx == M - 1:
#         count = visit[ny][nx][broken]
#         break
    
#     for i in range(4):
#         px = nx + dx[i]
#         py = ny + dy[i]
#         if 0 <= px < M\
#         and 0 <= py < N\
#         and visit[py][px][broken] == 0:
#             if gmap[py][px] == 1 and broken == 0: #벽 일때
#                 visit[py][px][1] = visit[ny][nx][0] + 1
#                 queue.append((px, py, 1))
#             elif gmap[py][px] == 0: #벽 아닐때
#                 visit[py][px][broken] = visit[ny][nx][broken] + 1
#                 queue.append((px, py, broken))

# print(count)

### 2D bfs

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visit = [[2] * M for _ in range(N)]
queue = deque([(0, 0, 1)])
answer = sys.maxsize
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit[0][0] = 0

while queue:
    x, y, d = queue.popleft()

    if x == M - 1 and y == N - 1:
        answer = d
        break

    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]

        if 0 <= px < M\
        and 0 <= py < N:
            b = visit[y][x] + graph[py][px]
            if b < visit[py][px]:
                visit[py][px] = b
                queue.append((px, py, d + 1))

if answer == sys.maxsize:    
    print(-1)
else:    
    print(answer)
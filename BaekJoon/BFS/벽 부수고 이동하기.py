"""
author: kyungmin
date: 23.12.07
title: 벽 부수고 이동하기
time: 30분
"""
import sys
input = sys.stdin.readline
from collections import deque
import copy

N, M = map(int, input().rstrip().split())
gmap = [[int(i) for i in input().rstrip()] for _ in range(N)]
queue = deque()
visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1
queue.append((0, 0, 0))
count = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    nx, ny, broken = queue.popleft()

    if ny == N - 1 and nx == M - 1:
        count = visit[ny][nx][broken]
        break
    
    for i in range(4):
        px = nx + dx[i]
        py = ny + dy[i]
        if 0 <= px < M\
        and 0 <= py < N\
        and visit[py][px][broken] == 0:
            if gmap[py][px] == 1 and broken == 0: #벽 일때
                visit[py][px][1] = visit[ny][nx][0] + 1
                queue.append((px, py, 1))
            elif gmap[py][px] == 0: #벽 아닐때
                visit[py][px][broken] = visit[ny][nx][broken] + 1
                queue.append((px, py, broken))

print(count)

#예외
# 011
# 001
# 110
# (x, y, 벽뚫안뚫?)
# 011
# 100
# 110
#어떤 경우가 다음 노드에 먼저 방문 할 것인지
# 5 8
# 01000000
# 01010000
# 01010000
# 01010011
# 00010010

# 0000000
# 0111111
# 0100010
# 0101010
# 0101010
# 0001010

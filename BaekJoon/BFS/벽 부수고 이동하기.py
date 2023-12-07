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
pmap = [[-1 if i == "1" else 0 for i in input().rstrip()] for _ in range(N)]
w_list = []
for y in range(N):
    for x in range(M):
        if pmap[y][x] == -1:
            w_list.append((x,y))
count = 100000000
signal = False
for i in range(-1, len(w_list)):
    gmap = copy.deepcopy(pmap)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    gmap[0][0] = 1
    queue.append((0,0))
    if i != -1:
        gmap[w_list[i][1]][w_list[i][0]] = 0
    while queue:
        nx, ny = queue.popleft()
        if ny == N - 1 and nx == M -1:
            count = min(gmap[ny][nx], count)
            signal = True
            break

        for i in range(4):
            px = nx + dx[i]
            py = ny + dy[i]
            if 0 <= px < M\
            and 0 <= py < N\
            and gmap[py][px] == 0:
                gmap[py][px] = gmap[ny][nx] + 1
                queue.append((px,py))

print(count if signal else -1)

#예외
# 011
# 001
# 110

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

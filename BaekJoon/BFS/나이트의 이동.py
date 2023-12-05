"""
author: kyungmin
date: 23.12.05
title: 나이트의 이동
time: 30분
"""
import sys
from collections import deque
input = sys.stdin.readline
test_case = int(input().rstrip())
result = []
for _ in range(test_case):
    N = int(input().rstrip())
    map1 = [[0] * N for _ in range(N)]

    sx, sy = map(int, input().rstrip().split())
    ex, ey = map(int, input().rstrip().split())
    if sx == ex and sy == ey:
        result.append(0)
        continue

    queue = deque()
    dx = [-2, -1, -2, -1, 1, 2, 1, 2]
    dy = [-1, -2, 1, 2, -2, -1, 2, 1]
    queue.append((sx, sy))
    map1[sy][sx] = 1
    count = 0
    while queue:
        nx, ny = queue.popleft()
        signal = False
        for i in range(8):
            px = nx + dx[i]
            py = ny + dy[i]
            if 0 <= px < N\
            and 0 <= py < N\
            and map1[py][px] == 0:
                map1[py][px] = map1[ny][nx] + 1
                queue.append((px, py))
                if px == ex and py == ey:
                    count = map1[ny][nx]
                    signal = True
                    break
        if signal:
            break
    result.append(count)

print(*result, sep='\n')

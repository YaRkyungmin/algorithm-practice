"""
author: kyungmin
date: 23.11.30
title: 불!
time: 30분
"""
import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

map = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(R):
    map.append(list(input().rstrip()))
queue = deque()
j_point = []
for y in range(R):
    for x in range(C):
        if map[y][x] == "F":
            queue.append([x, y, "F", 1])
        elif map[y][x] == "J":
            j_point = [x, y, "J", 1]
        else:
            continue

            continue
queue.append(j_point) # 불이 사람보다 더 빠름

result = 0
signal = False
while queue:
    [x, y, who, time] = queue.popleft()

    if who == "J":
        if x == 0 or x == C - 1 or y == 0 or y == R - 1:
            result = time
            signal = True
            break
    for i in range(4):
        if 0 <= x + dx[i] < C and 0 <= y + dy[i] < R and map[y + dy[i]][x + dx[i]] == ".":
            map[y + dy[i]][x + dx[i]] = who
            queue.append([x + dx[i], y + dy[i], who, time + 1])

if signal:
    print(result)
else:
    print("IMPOSSIBLE")
    

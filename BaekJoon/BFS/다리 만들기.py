"""
author: kyungmin
date: 23.12.10
title: 다리 만들기
time: 30분
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
group = [list(map(int, input().rstrip().split())) for _ in range(N)]
g_num = 1
queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[0 for _ in range(N)] for _ in range(N)]
genuine = deque()

def dfs():
    global g_num
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0 <= px < N\
            and 0 <= py < N\
            and visit[py][px] == 0\
            and group[py][px] == 1:
                group[py][px] = g_num
                visit[py][px] = 1
                queue.append((px, py))
                genuine.append((px, py))

for y in range(N):
    for x in range(N):
        if group[y][x] == 1 and visit[y][x] == 0:
            queue.append((x, y))
            group[y][x] = g_num
            genuine.append((x, y))
            visit[y][x] = 1
            dfs()
            g_num += 1
result = 10000000
def bfs():
    global result
    while genuine:
        x, y = genuine.popleft()
        p_num = group[y][x]
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]

            if 0 <= px < N\
            and 0 <= py < N:
                if group[py][px] == 0:
                    group[py][px] = p_num
                    visit[py][px] = visit[y][x] + 1
                    genuine.append((px, py))
                elif group[py][px] != p_num:
                    result = min(result, visit[y][x] + visit[py][px] - 2)
bfs()
print(result)

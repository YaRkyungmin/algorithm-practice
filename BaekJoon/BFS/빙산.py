"""
author: kyungmin
date: 23.12.09
title: 빙산
time: 30분
"""
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().rstrip().split())

mountain = [list(map(int, input().rstrip().split())) for _ in range(N)]
m_set = set()
for y in range(N):
    for x in range(M):
        if mountain[y][x] != 0:
            m_set.add((x, y))
c_year = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
accept = False
while True:
    zero_signal = False #빙산이 있는 지 체크
    n_mountain = [[0] * M for _ in range(N)]
    n_set = m_set.copy()
    visit = [[0] * M for _ in range(N)]
    count = 0
    for (x, y) in m_set:
        if mountain[y][x] != 0 and visit[y][x] == 0:
            count += 1 #빙산 수 세기
            zero_signal = True
            stack = []
            stack.append((x, y))
            visit[y][x] = 1
            while stack:
                w_count = 0
                nx, ny = stack.pop()
                for i in range(4):
                    px = nx + dx[i]
                    py = ny + dy[i]
                    if mountain[py][px] == 0:
                        w_count += 1
                    if 0 <= px < M\
                    and 0 <= py < N\
                    and mountain[py][px] != 0\
                    and visit[py][px] == 0:
                        visit[py][px] = 1
                        stack.append((px, py))
                if (mountain[ny][nx] - w_count) > 0: #새로운 빙산 생성
                    n_mountain[ny][nx] = (mountain[ny][nx] - w_count)
                else:
                    n_mountain[ny][nx] = 0
                    n_set.remove((nx,ny))
    if zero_signal == False: #다 녹았는데 안됐을때
        break
    if count >= 2:
        accept = True
        break
    mountain = n_mountain
    m_set = n_set
    c_year += 1
print(c_year if accept else 0) 
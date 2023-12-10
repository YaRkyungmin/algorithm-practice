"""
author: kyungmin
date: 23.12.10
title: 다리 만들기
time: 30분
"""
import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())

T = [list(map(int, input().rstrip().split())) for _ in range(N)]

min_c = 10000000
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0] * N for _ in range(N)] # 대륙찾아놓을때 그냥 지도 방문
for y in range(N):
    for x in range(N):
        if T[y][x] == 1 and visit[y][x] == 0:
            queue1 = deque()
            queue1.append((x, y)) 
            visit[y][x] = 1
            while queue1:
                nx, ny = queue1.popleft()
                for i in range(4):
                    px = nx + dx[i]
                    py = ny + dy[i]
                    if 0 <= px < N\
                    and 0 <= py < N\
                    and visit[py][px] == 0\
                    and T[py][px] == 1:
                        visit[py][px] = 1
                        queue1.append((px, py))

            queue2 = deque()
            queue2.append((x, y, 0))
            p_visit = [[0] * N for _ in range(N)] #바다지나는 방문
            p_visit[y][x] = 1
            signal = False
            while queue2:
                nx, ny, c = queue2.popleft()
                for i in range(4):
                    px = nx + dx[i]
                    py = ny + dy[i]
                    if 0 <= px < N\
                    and 0 <= py < N:
                        if T[py][px] == 1 and p_visit[py][px] == 0: # 대륙이고 방문 안했을 때
                            if c == 0: #국토일때
                                p_visit[py][px] = 1
                                queue2.append((px, py, c))
                            elif visit[py][px] == 0: #다른나라일때
                                min_c = min(c, min_c)
                        elif T[py][px] == 0: # 바다이고 방문 하거나 안했거나
                            if p_visit[py][px] == 0: # 누군가 지나가지 않은 바다 일때
                                p_visit[py][px] = c + 1
                                queue2.append((px, py, c + 1))
                            else: # 누군가 지나간 바다 일때
                                if c + 1 < p_visit[py][px]:
                                    p_visit[py][px] = c + 1
                                    queue2.append((px, py, c + 1))

print(min_c)
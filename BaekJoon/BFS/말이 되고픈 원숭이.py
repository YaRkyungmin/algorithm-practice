"""
author: kyungmin
date: 23.12.12
title: 말이 되고픈 원숭이
time: 30분
"""
import sys
input = sys.stdin.readline
from collections import deque

hx = [-2, -1, -2, -1, 1, 2, 1, 2]
hy = [1, 2, -1, -2, 2, 1, -2, -1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

K = int(input().rstrip())
W, H = map(int, input().rstrip().split())
T = [list(map(int, input().rstrip().split())) for _ in range(H)]

#(x, y, k 남은수, 이동수)
queue = deque([(0, 0, K, 0)])
#visit
visit = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
visit[0][0][K] = 1 
signal = False
m_move = 1000000000
while queue:
    nx, ny, k, m = queue.popleft()
    if nx == W - 1 and ny == H - 1:
        m_move = min(m, m_move)
        signal = True
        break

    if k > 0:
        for i in range(8):
            px = nx + hx[i]
            py = ny + hy[i]
            if 0 <= px < W\
            and 0 <= py < H\
            and visit[py][px][k - 1] == 0\
            and T[py][px] == 0:
                queue.append((px, py, k - 1, m + 1))
                visit[py][px][k - 1] = 1
    
    for i in range(4):
        px = nx + dx[i]
        py = ny + dy[i]
        if 0 <= px < W\
        and 0 <= py < H\
        and visit[py][px][k] == 0\
        and T[py][px] == 0:
            queue.append((px, py, k, m + 1))
            visit[py][px][k] = 1
            
print(m_move if signal else -1)
"""
author: kyungmin
date: 23.06.27
title: 미로 탐색
time: 30분
"""
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
queue = deque()

def bfs(sY, sX, eY, eX):
    queue.append((sY,sX))
    visit[sY][sX] = 1

    while queue:
        cY, cX = queue.popleft()

        if (cY, cX) == (eY, eX):
            return visit[eY][eX]

        for dY, dX in ((-1, 0), (1,0), (0,-1), (0,1)):
            nY, nX = cY + dY, cX + dX
            if 0<= nY < N and 0 <= nX < M and arr[nY][nX] == 1 and visit[nY][nX] == 0:
                queue.append((nY,nX))
                visit[nY][nX] = visit[cY][cX] + 1
        # 범위내, 4방향, 조건에 맞으면: arr= 1, v == 0

# 큐(Queue)의 활용: BFS는 큐를 사용하여 노드를 저장하고 탐색 순서를 유지합니다. 
# 각 레벨에서 인접한 노드들을 큐에 추가하고, 큐의 선입선출(FIFO) 특성에 따라 가장 가까운 노드부터 처리됩니다. 
# 이를 통해 최단 경로를 탐색할 수 있게 됩니다.
# 최단거리 BFS


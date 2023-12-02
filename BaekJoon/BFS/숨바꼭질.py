"""
author: kyungmin
date: 23.12.01
title: 숨바꼭질
time: 30분
"""
import sys
from collections import deque
N, K = map(int, input().rstrip().split())
queue = deque()
queue.append(N)
result = 0
visit = [0 for _ in range(100003)] # N이 K보다 작을 때를 생각해야함
while queue:
    n_point = queue.popleft()
    if n_point == K:
        result = visit[n_point]
        break
    if n_point - 1 >= 0 and visit[n_point-1] == 0:
        queue.append(n_point - 1)
        visit[n_point - 1] = visit[n_point] + 1
    if n_point + 1 <= K + 2 and visit[n_point+1] == 0:
        queue.append(n_point + 1)
        visit[n_point + 1] = visit[n_point] + 1
    if n_point * 2 <= K + 2 and visit[n_point*2] == 0:
        queue.append(n_point * 2)
        visit[n_point * 2] = visit[n_point] + 1

print(result)


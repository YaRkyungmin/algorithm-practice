"""
author: kyungmin
date: 23.12.11
title: 숨바꼭질 3
time: 30분
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
queue = deque()
queue.append((N, 0))
visit = [10000000 for _ in range(100003)]
visit[N] = 0
m_time = 10000000
while queue:
    nn, time = queue.popleft()
    if nn == K:
        continue

    if nn + 1 <= 100002\
    and visit[nn + 1] > time + 1:
        queue.append((nn + 1, time + 1))
        visit[nn + 1] = time + 1
        
    if nn - 1 >= 0\
    and visit[nn - 1] > time + 1:
        queue.append((nn - 1, time + 1))
        visit[nn - 1] = time + 1

    if nn * 2 <= 100002\
    and visit[nn * 2] > time:
        queue.appendleft((nn * 2, time))
        visit[nn * 2] = time
print(visit[K])
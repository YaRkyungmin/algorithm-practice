"""
author: kyungmin
date: 24.9.26
title: 숨바꼭질 4
time: 30분
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int ,input().rstrip().split())
visit = [-1 for _ in range(100001 + 1)]

queue = deque([N])

def check_root():
    c = K
    count = 0
    load = [K]
    while visit[c] != c:
        c = visit[c]
        count += 1
        load.append(c)
    print(count)
    print(*load[::-1])

visit[N] = N

while queue:
    node = queue.popleft()

    if node == K:
        check_root()
        break
    if 0 <= node - 1\
    and visit[node - 1] == -1:
        queue.append(node - 1)
        visit[node - 1] = node
    if node + 1 <= K + 1\
    and visit[node + 1] == -1:
        queue.append(node + 1)
        visit[node + 1] = node
    if node * 2 <= K + 1\
    and visit[node * 2] == -1:
        queue.append(node * 2)
        visit[node * 2] = node

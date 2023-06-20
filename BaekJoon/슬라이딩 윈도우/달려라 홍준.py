"""
author: kyungmin
date: 23.06.20
title: 달려라 홍준
time: 30분
"""
from collections import deque
N, M = map(int, input().split())
arr = list(map(int, input().split()))
d = deque()

for i in range(2*M - 2):
    while d and d[-1][1] < arr[i]:
        d.pop()
    d.append((i,arr[i]))

for i in range(2*M - 2, N):
    while d and d[-1][1] < arr[i]:
        d.pop()
    d.append((i,arr[i]))
    if d[0][0] <= (i-2*M+1):
        d.popleft()
    print(d[0][1], end=" ")

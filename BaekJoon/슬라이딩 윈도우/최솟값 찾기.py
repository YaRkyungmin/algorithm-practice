"""
author: kyungmin
date: 23.06.19
title: 최솟값 찾기
time: 30분
"""
# 1 5 2 3 6 2 3 7 3 5 2 6
from collections import deque
N, L = map(int, input().split())
arr = list(map(int, input().split()))
d = deque()
result = []
for i in range(N):
    while d and d[-1][1] >= arr[i]:
        d.pop()
    d.append((i,arr[i]))
    if d[0][0] == i - L :
        d.popleft()
    result.append(d[0][1])
print(*result)
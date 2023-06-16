"""
author: kyungmin
date: 23.06.13
title: 구간 합 구하기 5
time: 30분
"""
# 행을 구하고 열을 구하면 쉬움!
N, M = map(int, input().split())
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
sa = [[0 for i in range(N+1)] for _ in range(N+1)]
for y in range(1,N+1):
    for x in range(1,N+1):
        sa[y][x] = sa[y][x-1] + sa[y-1][x] - sa[y-1][x-1] + a[y-1][x-1]

r = []
for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    r.append(sa[y2][x2] - sa[y1-1][x2] - sa[y2][x1-1] + sa[y1-1][x1-1])
    
for i in r:
    print(i)

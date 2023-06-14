"""
author: kyungmin
date: 23.06.14
title: 2차원 배열의 합
time: 30분
"""

N, M = map(int, input().split())
a = []
sa_r = [[0]*M for _ in range(N)]
sa_RR = [[0]*M for _ in range(N)]

sa_c = [[0]*(M+1) for _ in range(N+1)]
r = []
for _ in range(N):
    a.append(list(map(int, input().split())))

for y in range(N):
    sum = 0
    for x in range(M):
        sum += a[y][x]
        sa_r[y][x] = sum

for x in range(M):
    sum = 0
    for y in range(N):
        sum += sa_r[y][x]
        sa_c[y+1][x+1] = sum

K = int(input())

for _ in range(K):
    i, j, x, y = list(map(int, input().split()))
    
    r.append(sa_c[x][y] - sa_c[i-1][y] - sa_c[x][j-1] + sa_c[i-1][j-1])

for i in range(K):
    print(r[i])


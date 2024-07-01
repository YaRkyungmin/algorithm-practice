"""
author: kyungmin
date: 24.7.1
title: 플로이드
time: 30분
"""
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize
n = int(input().rstrip()) # vertex 갯수
m = int(input().rstrip()) # vertex 갯수

d = [[MAX_INT] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    d[a - 1][b - 1] = min(d[a - 1][b - 1], c)
for i in range(n):
    d[i][i] = 0

for z in range(n):
    for s in range(n):
        for t in range(n):
            d[s][t] = min(d[s][z] + d[z][t], d[s][t])

for y in range(n):
    for x in range(n):
        if d[y][x] == MAX_INT:
            d[y][x] = 0

for i in d:
    print(" ".join(map(str, i)))

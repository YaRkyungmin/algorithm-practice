"""
author: kyungmin
date: 23.06.13
title: 구간 합 구하기 4
time: 30분
"""
N, M = map(int, input().split())
a = list(map(int, input().split()))
l = []
sa = [0 for _ in range(N+1)]
s = 0
for i in range(N):
    s += a[i]
    sa[i+1] = s

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    l.append(sa[j]-sa[i])
for i in l:
    print(i)
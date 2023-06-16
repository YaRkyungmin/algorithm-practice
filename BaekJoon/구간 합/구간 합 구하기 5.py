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

1 1 1
1 1 1
1 1 1
0 0 0 0 
0 0 0 0
0 0 0 0
0 0 0 0
sa = []

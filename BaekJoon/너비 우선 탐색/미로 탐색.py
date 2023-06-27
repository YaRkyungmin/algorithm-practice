"""
author: kyungmin
date: 23.06.27
title: 미로 탐색
time: 30분
"""
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = deque([[0]]) * (N + 1)
graph[0] = [0] * M
for x in range(N):
    s = list(input())
    [1,2,3,4]
    for i in list(s):
        graph[x+1].append(i)
print(graph)
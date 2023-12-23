"""
author: kyungmin
date: 23.12.22
title: N과 M (1)
time: 30분
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [0 for _ in range(M)]
visit = [False for _ in range(N + 1)]

def permutatation(k):
    global N, M
    if k == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if not visit[i]:
            arr[k] = i
            visit[i] = True
            permutatation(k + 1)
            visit[i] = False

permutatation(0)
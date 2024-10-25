"""
author: kyungmin
date: 24.10.15
title: 점프
time: 30분
"""
import sys
input = lambda: sys.stdin.readline().rstrip()
MAX_INT = sys.maxsize

N, M = map(int, input().split())
max_k = int((2 * N) ** 0.5) + 1
dp = [[MAX_INT] * (max_k + 1) for _ in range(N)]
dp[0][0] = 0

out = set()
for _ in range(M):
    out_rock = int(input())
    out.add(out_rock - 1)

for i in range(1, N):
    if i in out:
        continue
    for v in range(1, int((i * 2) ** 0.5) + 1):
        dp[i][v] = min(dp[i - v][v - 1], dp[i - v][v], dp[i - v][v + 1]) + 1

answer = min(dp[N - 1])

if answer == MAX_INT:
    print(-1)
else:
    print(answer)
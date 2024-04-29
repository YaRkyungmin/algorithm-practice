"""
author: kyungmin
date: 24.4.29
title: 스타트와 링크
time: 30분
"""
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize
result = MAX_INT

N = int(input().rstrip())
stat = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [False for _ in range(N)]
result
def find_team(cnt, numbers):
    if numbers == N // 2:
        a_team = []
        b_team = []
        for i in range(N):
            if dp[i]:
                a_team.append(i)
            else:
                b_team.append(i)
        check_diff(a_team, b_team)

    for i in range(cnt, N):
        dp[i] = True
        find_team(i + 1, numbers + 1)
        dp[i] = False
def check_diff(a, b):
    global result
    a_sum = 0
    b_sum = 0
    for x in range(N//2):
        for y in range(N//2):
            if x == y:
                continue
            a_sum += stat[a[x]][a[y]]
            b_sum += stat[b[x]][b[y]]

    diff_sum = abs(a_sum - b_sum)
    result = min(result, diff_sum)
find_team(0, 0)

print(result)
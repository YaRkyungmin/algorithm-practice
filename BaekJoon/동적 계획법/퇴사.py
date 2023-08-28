"""
author: kyungmin
date: 23.08.29
title: 퇴사
time: 30분
"""

import sys
input = sys.stdin.readline
# 6 5 4 3 2 1 0
N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
# 0 1 2 3 4 5 6

dp = [0 for _ in range(N+1)]
# 0 1 2 3 4 5 6 7

for i in range(N-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
    if i + li[i][0] > N:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        no_sangdam = dp[i+1]
        sangdam = li[i][1] + dp[i + li[i][0]]

        dp[i] = max(no_sangdam, sangdam)

print(dp[0])
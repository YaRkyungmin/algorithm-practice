"""
author: kyungmin
date: 23.08.29
title: 정수를 1로 만들기
time: 30분
"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = {1: 0}

def top_down(n):
    if n in dp.keys():
        return dp[n]
    if (n % 3 == 0) and (n % 2 == 0):
        dp[n] = min(top_down(n // 3) + 1, top_down(n // 2) + 1)
    elif n % 3 == 0:
        dp[n] = min(top_down(n // 3) + 1, top_down(n - 1) + 1)
    elif n % 2 == 0:
        dp[n] = min(top_down(n // 2) + 1, top_down(n - 1) + 1)
    else:
        dp[n] = top_down(n - 1) + 1
    return dp[n]

print(top_down(N))
"""
author: kyungmin
date: 24.2.10
title: 피보나치 수의 확장
time: 30분
"""
import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 0

if n < 0:
    dp = [0, 1] + [0 for i in range(0, abs(n))]
    for i in range(-1, -1 + n, -1):
        p = dp[i + 2] - dp[i + 1]
        if p > 0:
            dp[i] = p % 1000000000
        else:
            dp[i] = (-p % 1000000000) * -1
    result = dp[n]
else:
    dp = [0, 1] + [0 for i in range(1, n)]
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
    result = dp[n]

if result > 0:
    print(1)
    print(result)
elif result == 0:
    print(0)
    print(result)
else:
    print(-1)
    print(abs(result))


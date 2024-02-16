"""
author: kyungmin
date: 24.2.16
title: 암호코드
time: 30분
"""
import sys
input = sys.stdin.readline

code = list(map(int, input().rstrip()))

dp = [[1, 0]] + [[0,0] for _ in range(len(code) - 1)]
result = 0
signal = True
if code[0] == 0:
    signal = False
else:
    for i in range(1, len(code)):
        rs = True
        if code[i] == 0:
            if 0 < code[i - 1] * 10 + code[i] <= 20: # 중간에 0이 들어간 예외
                dp[i][0] = dp[i - 1][0]
                rs = False
            else:
                signal = False
                break
        if rs:
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            if code[i - 1] == 0:
                dp[i][0] = dp[i - 1][0]
            else:
                if code[i - 1] * 10 + code[i] <= 26:
                    dp[i][1] = dp[i - 1][0]
if signal:
    result = dp[len(code) - 1][0] + dp[len(code) - 1][1]
if len(code) == 1\
and signal:
    result = 1

print(result % 1000000)
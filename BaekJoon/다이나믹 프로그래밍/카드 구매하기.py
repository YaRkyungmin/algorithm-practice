"""
author: kyungmin
date: 24.2.5
title: 카드 구매하기
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split())) # 1 5 6 7
dp = list(numbers)
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        dp[i] = max(dp[i], dp[j] + numbers[i - j - 1])

print(dp[N - 1])
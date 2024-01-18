"""
author: kyungmin
date: 24.1.19
title: 쉬운 계단 수
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [0 for _ in range(N)]
numbers = [1 for _ in range(10)]
numbers[0] = 0

for i in range(N):
    sum = 0
    for x in range(10):
        sum += numbers[x]
    dp[i] = sum % 1000000000

    newNum = [0 for _ in range(10)] 
    newNum[0] = numbers[1] % 1000000000
    newNum[9] = numbers[8] % 1000000000
    for n in range(1, 9):
        newNum[n] = (numbers[n - 1] + numbers[n + 1]) % 1000000000
    
    numbers = newNum

print(dp[N - 1])

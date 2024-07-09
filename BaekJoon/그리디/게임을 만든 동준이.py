"""
author: kyungmin
date: 24.07.09
title: 게임을 만든 동준이
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

numbers = [int(input().rstrip()) for _ in range(N)]
m = numbers[N - 1]
result = 0
for i in range(N - 2, -1, -1):
    while m <= numbers[i]:
        numbers[i] -= 1
        result += 1 
    m = numbers[i]
print(result)
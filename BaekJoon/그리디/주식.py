"""
author: kyungmin
date: 24.07.16
title: 주식
time: 30분
"""
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    numbers = list(map(int, input().rstrip().split()))
    result = 0
    pick = numbers[N - 1]
    for i in range(N - 2, -1, -1):
        if pick > numbers[i]:
           result += pick - numbers[i]
        elif pick < numbers[i]:
           pick = numbers[i]
    
    print(result)
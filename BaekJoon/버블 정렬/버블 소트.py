"""
author: kyungmin
date: 23.07.15
title: 버블 소트
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = [(int(input()), i) for i in range(N)]
numbers.sort()

max = 0
for i in range(N):
    if max < numbers[i][1] - i:
        max = numbers[i][1] - i
print(max+1)

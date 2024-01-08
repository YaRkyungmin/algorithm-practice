"""
author: kyungmin
date: 24.1.9
title: 좌표 정렬하기2
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = []

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    numbers.append((x, y))

numbers.sort(key = lambda x: (x[1], x[0]))
for (x, y) in numbers:
    print(f"{x} {y}")
"""
author: kyungmin
date: 24.2.23
title: 부분합
time: 30분
"""
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize

N, S = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
s = 0
e = 0
result = MAX_INT
sum_numbers = 0

while e < N + 1:
    if sum_numbers < S:
        if e == N:
            break
        sum_numbers += numbers[e]
        e += 1
    else:
        result = min(e - s, result)
        sum_numbers -= numbers[s]
        s += 1

print(result if result != MAX_INT else 0)
    
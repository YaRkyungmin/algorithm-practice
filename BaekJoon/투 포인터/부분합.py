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
sum_numbers = numbers[0]
signal = False
while e < N - 1 or s <= e:
    if sum_numbers < S:
        if e == N - 1:
            break
        e += 1
        sum_numbers += numbers[e]
    else:
        signal = True
        result = min(result, e - s + 1)
        sum_numbers -= numbers[s]
        s += 1

print(result if signal else 0)
    
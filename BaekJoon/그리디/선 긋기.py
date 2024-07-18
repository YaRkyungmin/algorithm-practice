"""
author: kyungmin
date: 24.07.19
title: 선 긋기
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

numbers = [list(map(int, input().rstrip().split())) for _ in range(N)]
numbers.sort()
result = numbers[0][1] - numbers[0][0]
pick = numbers[0][1]
for i in range(1, N):
    if pick >= numbers[i][0]:
        if pick <= numbers[i][1]:
            result += numbers[i][1] - pick
            pick = numbers[i][1]
    else:
        result += numbers[i][1] - numbers[i][0]
        pick = numbers[i][1]
print(result)
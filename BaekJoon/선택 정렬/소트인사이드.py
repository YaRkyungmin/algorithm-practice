"""
author: kyungmin
date: 23.07.12
title: 소트인사이드
time: 30분
"""
import sys
input = sys.stdin.readline

numbers = list(input().rstrip())
for x in  range(len(numbers)):
    min_value_index = 0
    for y in range(len(numbers)-x):
        if numbers[min_value_index] > numbers[y]:
            min_value_index = y
    N = len(numbers)-x-1
    numbers[N], numbers[min_value_index] = numbers[min_value_index], numbers[N]

for i in range(len(numbers)):
    print(numbers[i], end="")   
"""
author: kyungmin
date: 23.07.01
title: 수 찾기
time: 20분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().split()))
M = int(input().rstrip())
search_numbers = list(map(int, input().split()))
numbers.sort()
for num in search_numbers:
    start = 0
    end = N - 1
    flag = 0
    while start <= end:
        median = (start + end) // 2
        if numbers[median] < num:
            start = median + 1
        elif numbers[median] > num:
            end = median - 1
        else:
            flag = 1
            break
    print(flag)
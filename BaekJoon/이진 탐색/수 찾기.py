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

for i in range(M):
    sn = search_numbers[i]
    start = 0
    end = len(numbers) -1
    flag = 0
    while start <= end:
        midian = (start + end) // 2
        if numbers[midian] > sn :
            end = midian -1
        elif numbers[midian] < sn :
            start = midian + 1
        else:
            flag = 1
            break
    print(flag)
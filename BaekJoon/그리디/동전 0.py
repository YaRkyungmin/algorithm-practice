"""
author: kyungmin
date: 23.07.09
title: 동전 0
time: 30분
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(int(input().rstrip()))
num_sum = K
num_cnt = 0
for i in range(-1, -(N + 1), -1):
    cnt = num_sum // numbers[i]
    num_sum -= cnt * numbers[i]
    num_cnt += cnt
    if num_sum == 0:
        break
print(num_cnt)
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
num_sum = 0
cnt = 0 

for i in range(-1, -(N + 1), -1):
    if numbers[i] <= K:
        while num_sum <= K:
            num_sum += numbers[i]
            cnt += 1
        num_sum -= numbers[i]
        cnt -= 1
    if num_sum == K:
        break
print(cnt)
"""
author: kyungmin
date: 24.2.25
title: 수들의 합 2
time: 30분
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
st = 0
en = 0
p_sum = 0
result = 0
while en <= N:
    if p_sum < M:
        if en == N:
            break
        p_sum += numbers[en]
        en += 1
    else:
        if p_sum == M:
            result += 1
        p_sum -= numbers[st]
        st += 1
        
print(result)
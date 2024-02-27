"""
author: kyungmin
date: 24.2.27
title: 가장 긴 짝수 연속한 부분 수열 (large)
time: 30분
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
st = 0
en = 0
p_sum = 0
result = 0

while en < N:
    if numbers[en] % 2 == 0:
        p_sum += 1
        en += 1
    else:
        if K > 0:
            K -= 1
            en += 1
        else:
            result = max(result, p_sum)
            if numbers[st] % 2 == 0:
                p_sum -= 1
            else:
                K += 1
            st += 1
result = max(result, p_sum)
print(result)
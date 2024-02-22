"""
author: kyungmin
date: 24.2.22
title: 수 고르기
time: 30분
"""
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize

N, M = map(int, input().rstrip().split())
numbers = [int(input().rstrip()) for _ in range(N)]
numbers.sort()
s = 0
e = 0
result = MAX_INT
while e < N:
    patial_result = numbers[e] - numbers[s]
    if patial_result < M:
        e += 1
    elif patial_result == M:
        result = M
        break
    else:
        s += 1
        result = min(patial_result, result)

print(result)
        

    
    
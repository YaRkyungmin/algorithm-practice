"""
author: kyungmin
date: 24.07.09
title: 보물
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
a_numbers = list(map(int, input().rstrip().split()))
b_numbers = list(map(int, input().rstrip().split()))

a_numbers.sort()
b_numbers.sort(reverse=True)
S = 0
for i in range(N):
    S += a_numbers[i] * b_numbers[i]

print(S)
"""
author: kyungmin
date: 23.06.15
title: 나머지 합
time: 30분
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

a = list(map(int, input().split()))
s_a = [0 for i in range(N)]
##
s = 0
for i in range(N):
    s += a[i]
    s_a[i] = s

result = 0
s_a_r = [i%M for i in s_a]
r_array = [0 for i in range(M)]

for i in range(N):
    r_array[s_a_r[i]] += 1

result += r_array[0]
for i in r_array:
    if i > 1:
        result += int(i*(i-1)/2) 
print(result)
"""
author: kyungmin
date: 23.06.12
title: 숫자의 합 구하기
time: 15분
"""
import sys
input = sys.stdin.readline
N = int(input())

a = input()
sum = 0
for z in range(N) :
    sum += int(a[z])
print(sum)
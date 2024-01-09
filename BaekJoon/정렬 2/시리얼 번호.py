"""
author: kyungmin
date: 24.1.10
title: 시리얼 번호
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

serial = []
judge = dict()

for _ in range(N):
    S = input().rstrip()
    serial.append(S)
    sum = 0
    for i in S:
        if 49 <= ord(i) <= 57:
            sum += int(i)
    judge[S] = sum


serial.sort(key=lambda x: (len(x), judge[x], x))
print(*serial, sep = "\n")

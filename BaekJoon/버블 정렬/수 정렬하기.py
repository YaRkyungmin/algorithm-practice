"""
author: kyungmin
date: 23.07.12
title: 수 정렬하기
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = [int(input().rstrip()) for _ in range(N)]

if len(numbers) > 1:
    for x in range(N):
        for y in range(N-x-1):
            lhd = numbers[y]
            rhd = numbers[y + 1]
            if lhd > rhd:
                numbers[y], numbers[y+1] = rhd, lhd
for i in numbers:
    print(i)
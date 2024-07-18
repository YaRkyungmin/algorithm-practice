"""
author: kyungmin
date: 24.07.18
title: 카드 합체 놀이
time: 30분
"""
import sys
input = sys.stdin.readline
from heapq import *

n, m = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

heapify(numbers)

for _ in range(m):
    a = heappop(numbers)
    b = heappop(numbers)
    s = a + b
    heappush(numbers, s)
    heappush(numbers, s)
print(sum(numbers))

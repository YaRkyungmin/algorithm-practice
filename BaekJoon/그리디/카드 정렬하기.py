"""
author: kyungmin
date: 23.07.09
title: 카드 정렬하기
time: 30분
"""
import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
heap = []
for _ in range(N):
    heapq.heappush(heap,int(input().rstrip()))
sum = 0
while len(heap) > 1:
    element_one = heapq.heappop(heap)
    element_two = heapq.heappop(heap)
    sum += element_one + element_two
    heapq.heappush(heap, element_one + element_two)
print(sum)
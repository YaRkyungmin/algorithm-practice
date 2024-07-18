"""
author: kyungmin
date: 24.07.18
title: 강의실 배정
time: 30분
"""
import sys
import heapq
input = sys.stdin.readline
heap = []

N = int(input().rstrip())

cls = [list(map(int, input().rstrip().split())) for _ in range(N)]

cls.sort()

for i in cls:
    if heap:
        if heap[0] <= i[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, i[1])
        else:
            heapq.heappush(heap, i[1])
    else:
        heapq.heappush(heap, i[1])

print(len(heap))


"""
author: kyungmin
date: 23.07.10
title: 카드 정렬하기
time: 30분
"""
import sys
import heapq
input = sys.stdin.readline
N = int(input().rstrip())
time = []
for _ in range(N):
    A, B = map(int, input().split())
    heapq.heappush(time, (B,A))

end_time = 0
cnt = 0
while time:
    end, start = heapq.heappop(time)
    if start >= end_time:
        end_time = end
        cnt += 1
print(cnt)



"""
author: kyungmin
date: 24.2.29
title: 겹치는 건 싫어
time: 30분
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
st = 0
en = 0
visited = [0 for _ in range(1000001)]
result = 0

while en < N:
    if visited[numbers[en]] < K: # 방문한적이 K 보다 작을때
        visited[numbers[en]] += 1
        en += 1
    else:
        result = max(result, en - st)        
        visited[numbers[st]] -= 1
        st += 1
result = max(result, en - st)
print(result)
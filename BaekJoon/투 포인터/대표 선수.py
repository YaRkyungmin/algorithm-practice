"""
author: kyungmin
date: 24.3.1
title: 대표 선수
time: 30분
"""
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize

# heap을 이용해서 복습풀이 해보자!
N, M = map(int, input().rstrip().split())
numbers = []
for i in range(N):
    for l in list(map(int, input().rstrip().split())):
        numbers.append((l, i))

visited = [0 for _ in range(N)]
numbers.sort()
st = 0
en = 0
p_cl = 0
result = MAX_INT

while en <= N * M:
    if p_cl < N:
        if en == N * M:
            break
        if visited[numbers[en][1]] == 0:
            p_cl += 1
        visited[numbers[en][1]] += 1        
        en += 1
    else:
        result = min(result, numbers[en - 1][0] - numbers[st][0])
        visited[numbers[st][1]] -= 1
        if visited[numbers[st][1]] == 0:
            p_cl -= 1
        st += 1

print(result)
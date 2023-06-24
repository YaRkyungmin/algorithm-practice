"""
author: kyungmin
date: 23.06.21
title: 오큰수
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

result = [-1 for _ in range(N)]
stack = []
for i in range(N):
    while stack and numbers[i] > numbers[stack[-1]] :
        node_index = stack.pop()
        result[node_index] = numbers[i]
    stack.append(i)
print(*result)

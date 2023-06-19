"""
author: kyungmin
date: 23.06.19
title: 최솟값 찾기
time: 30분
"""
N, L = map(int, input().split())
arr = list(map(int, input().split()))
minValue = arr[0]
result = f"{minValue}"

for i in range(1, L):
    if arr[i] < minValue:
        minValue = arr[i]
    result += f" {minValue}"

for i in range(L, N):
    if arr[i] <= minValue:
        minValue = arr[i]
    elif arr[i-L] == minValue:
        minValue = min(arr[i-L+1:i+1])
    result += f" {minValue}"
print(result)


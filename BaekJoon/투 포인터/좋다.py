"""
author: kyungmin
date: 23.06.17
title: 좋다
time: 30분
"""
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
for i in range(N):
    start = 0
    end = N-1
    while start != end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        if arr[i] == arr[start] + arr[end]:
            result += 1
            break
        elif arr[i] < arr[start] + arr[end]:
            end -= 1
        else:
            start += 1
print(result)
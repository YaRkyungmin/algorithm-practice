"""
author: kyungmin
date: 23.06.13
title: 구간 합 구하기 4
time: 30분
"""
N, M = map(int, input().split())
a = list(map(int, input().split()))
sumArray = [0]
sum = 0
for i in range(0, N):
    sum += a[i]
    sumArray.append(sum)
# 5 4 3 2 1
# 0 5 9 12 14 15
for _ in range(0, M):
    i, j = map(int, input().split())
    print(sumArray[j-1] - sumArray[i-2])
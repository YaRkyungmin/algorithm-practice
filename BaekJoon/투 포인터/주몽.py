"""
author: kyungmin
date: 23.06.16
title: 주몽
time: 30분
"""
N = int(input())
M = int(input())
#N 갯수, M 합
l = list(map(int, input().split()))
l.sort()
count = 0
# 1 2 3 4 5 7
start = 0
end = N - 1
while start != end :
    sum = l[start] + l[end]
    if sum == M:
        count += 1
        start += 1
    elif  sum < M:
        start += 1
    else:
        end -= 1
print(count)
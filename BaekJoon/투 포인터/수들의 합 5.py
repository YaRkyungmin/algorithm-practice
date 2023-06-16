"""
author: kyungmin
date: 23.06.16
title: 수들의 합 5
time: 30분
"""
N = int(input())

start = 1
end = 1
count = 1
sum = 1

while start < N :
    if sum == N:
        count += 1
        end += 1
        sum += end
    elif sum < N:
        end += 1
        sum += end
    else :
        sum -= start
        start += 1

print(count)

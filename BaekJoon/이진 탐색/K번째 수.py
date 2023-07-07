"""
author: kyungmin
date: 23.07.06
title: K번째 수
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
start = 1
end = N * N
result = 1
while start < end:
    mid = (start + end) // 2
    sum_num = 0
    for i in range(1, N + 1):
        cnt = mid // i
        if cnt > N:
            sum_num += N
        else:
            sum_num += cnt
    if sum_num < K:
        start = mid + 1
    elif sum_num > K:
        end = mid - 1
    else:
        result = mid
        break
if start >= end:
    print(start)
else:
    print(result)
# 1 2 3 3
# 2 4 6 3
# 3 6 9 2

# 1 2 2 3 3 4 6 6 9

# 1 2 3 4 5m 6s 7m 8 9e
"""
author: kyungmin
date: 23.06.16
title: 주몽
time: 30분
"""
N = int(input())
M = int(input())

l = list(map(int, input().split()))
count = 0
for i in range(0,N):
    for x in range(i+1,N):
        if l[i] + l[x] == M :
            count += 1
print(count)
# if N < 2:
#     print(0)
# s = 0
# e = 1
# count = 0
# sum = l[s]
# print(l)
# while s < N: # 1 2 3 4 5 7
#     sum += l[e]
#     print(sum)
#     if sum == M:
#         count += 1
#         sum -= l[e]
#         e += 1
#     elif sum < M:
#         sum -= l[e]
#         e += 1
#     else:
#         sum -= l[s]
#         s += 1
#         if s < e :
#             sum += l[s]
#         else :
#             break

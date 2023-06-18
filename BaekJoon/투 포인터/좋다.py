"""
author: kyungmin
date: 23.06.17
title: 좋다
time: 30분
"""
# N = int(input())
# l = list(map(int, input().split()))
# l.sort()
# count = 0
# #2 2 2 2 4 4 8 8
# if N > 2 :
#     for i in range(N-1,1,-1):
#         result = l[i]
#         start = 0
#         end = i - 1 
#         while start != end :
#             sum = l[start] + l[end]
#             if sum == result:
#                 count += 1
#                 break
#             elif sum > result:
#                 end -= 1
#             else:
#                 start += 1
#     print(count)
# else:
#     print(count)
# 1 2 3 4 5 6
# 1 2 3 4 5 6
N = int(input())
S = list(map(int, input().split()))
S.sort()
cnt = 0
# 1 1 2 2 3 4 5
# -5 -3 -2
for i in range(N):
    start = 0
    end = N-1
    while start != end:
        if start != i and end != i:
            if S[start]+S[end] == S[i]:
                cnt += 1
                break
            elif S[start]+S[end] > S[i]:
                end -= 1
            else:
                start += 1
        else:
            if start == i:
                start += 1
            else:
                end -= 1
print(cnt)
"""
author: kyungmin
date: 24.4.22
title: 같이 눈사람 만들래?
time: 30분
"""
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize
N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()
result = MAX_INT
signal = True
for i in range(N - 3):
    if not signal:
            break
    
    for j in range(i + 3, N):
        A = numbers[i] + numbers[j]
        st = i + 1
        en = j - 1
        while st < en and en < j:
            B = numbers[st] + numbers[en]
            diff = A - B
            if A > B:
                result = min(result, abs(diff))
                st += 1
            elif A < B:
                result = min(result, abs(diff))
                en -= 1
            else:
                result = 0
                signal = False
                break
        
        if not signal:
            break

print(result)

# import sys
# input = sys.stdin.readline
# MAX_INT = sys.maxsize
# N = int(input().rstrip())
# numbers = list(map(int, input().rstrip().split()))
# numbers.sort()
# snowman = []

# for i in range(N):
#     for j in range(i + 1, N):
#         snowman.append((numbers[i] + numbers[j], i, j))

# snowman.sort()
# s_len = len(snowman)
# result = MAX_INT

# for i in range(s_len):
#     for j in range(i, s_len):
#         if snowman[i][1] != snowman[j][1]\
#         and snowman[i][1] != snowman[j][2]\
#         and snowman[i][2] != snowman[j][1]\
#         and snowman[i][2] != snowman[j][2]:
#             result = min(result, snowman[j][0] - snowman[i][0])
        
# print(result)

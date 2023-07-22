"""
author: kyungmin
date: 23.07.22
title: 거의 소수
time: 30분
"""
import sys
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())

max_numbers = int(B**.5)+1
numbers = [True]*(max_numbers + 1)
numbers[1] = False

for i in range(2,int(max_numbers**.5)+1):
    if not numbers[i]:
        continue
    x = 2
    while i * x <= max_numbers:
        numbers[i * x] = False
        x += 1


cnt = 0

for i in range(1, max_numbers+1):
    if numbers[i]:
        x = i * i
        while x <= B:
            if A <= x <= B:
                cnt += 1
            x *= i
print(cnt)


# def search_prime_number(N):
#     if N > 1:
#         for i in range(2,int(N**.5)+1):
#             if N % i == 0:
#                 return False
#         return True
#     else:
#         return False

# cnt = 0

# for i in range(A, B+1):
#     if search_prime_number(i):
#         x = i * i
#         while x <= B:
#             cnt += 1
#             x *= i            

# print(cnt)


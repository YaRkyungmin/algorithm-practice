"""
author: kyungmin
date: 23.06.23
title: 소수 구하기
time: 30분
"""
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

prime_numbers = []

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(M, N+1):
    if i == 1:
        continue
    if isPrime(i):
        print(i)

# import sys
# input = sys.stdin.readline

# M, N = map(int, input().split())
# true_false_list = [True] * (N+1)
# true_false_list[1] = False

# for i in range(2, int(N**0.5) + 1):
#     if true_false_list[i] == True:
#         for j in range(2 * i, N+1, i):
#             true_false_list[j] = False

# for i in range(M, N+1):
#     if true_false_list[i]:
#         print(i)
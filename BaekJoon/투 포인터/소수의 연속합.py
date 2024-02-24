"""
author: kyungmin
date: 24.2.24
title: 소수의 연속합
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = [True for _ in range(N + 1)]

def check_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if numbers[i]:
            j = 2
            while i * j <= num:
                numbers[i * j] = False
                j += 1
check_prime(N)
prime_numbers = []

for i in range(2, N + 1):
    if numbers[i]:
        prime_numbers.append(i)

if prime_numbers:
    st = 0
    en = 0
    p_sum = 0
    result = 0
    while en <= len(prime_numbers):
        if p_sum < N:
            if en == len(prime_numbers):
                break
            p_sum += prime_numbers[en]
            en += 1
        else:
            if p_sum == N:
                result += 1
            p_sum -= prime_numbers[st]
            st += 1
    print(result)
else:
    print(0)

"""
author: kyungmin
date: 23.07.26
title: GCD(n, k) = 1
time: 30분
"""
import sys
input = sys.stdin.readline

n = int(input().rstrip())
N = int(n**.5) + 1
prime_numbers = [True] * (N+1)

def configure_prime_numbers(n):
    prime_numbers[0] = False
    prime_numbers[1] = False
    for i in range(2, int(n**.5)+1):
        if prime_numbers[i]:
            M = 2
            while (M * i) <= n:
                prime_numbers[M * i] = False
                M += 1

def check_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**.5)+1):
        if number % i == 0:
            return False
    return True

configure_prime_numbers(N)

cnt = n

if check_prime_number(n):
    cnt -= 1

for i in range(2,N+1):
    if prime_numbers[i] == True and n % i == 0:
        cnt = cnt - int(cnt/i)

print(cnt)


# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())

# def check_prime_number(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**.5)+1):
#         if number % i == 0:
#             return False
#     return True


# cnt = n
# for i in range(2,n+1):
#     if check_prime_number(i) and n % i == 0:
#         cnt = cnt - int(cnt/i)

# print(cnt)
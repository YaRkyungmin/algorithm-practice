"""
author: kyungmin
date: 23.07.11
title: 수 묶기
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
zero_numbers = []
numbers = []
negative_numbers = []

for _ in range(N):
    k = int(input().rstrip())
    if k == 0:
        zero_numbers.append(k)
    elif k > 0 == 0:
        numbers.append(k)
    else:
        negative_numbers.append(k)

numbers.sort()
negative_numbers.sort()

sum_numbers = 0

if len(numbers) % 2 == 1:
    while len(numbers) > 1:
        a = numbers.pop()
        b = numbers.pop()
        if b != 1:
            sum_numbers += (a * b)
        else:
            sum_numbers += a + b
    sum_numbers += numbers.pop()
else:
    while numbers:
        a = numbers.pop()
        b = numbers.pop()
        if b != 1:
            sum_numbers += (a * b)
        else:
            sum_numbers += a + b

if len(negative_numbers) % 2 == 1:
    if zero_numbers:
        negative_numbers.pop()
    else:
        sum_numbers += negative_numbers.pop()
    while negative_numbers:
        sum_numbers += (negative_numbers.pop() * negative_numbers.pop())
else:
    while negative_numbers:
        sum_numbers += (negative_numbers.pop() * negative_numbers.pop())

print(sum_numbers)
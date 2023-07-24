"""
author: kyungmin
date: 23.07.24
title: 제곱 ㄴㄴ 수
time: 30분
"""
import sys
input = sys.stdin.readline

min_value, max_value = map(int, input().rstrip().split())

numbers_len = max_value - min_value + 1
numbers = [1] * numbers_len

for i in range(2, int(max_value**.5) + 1):
    mul_num = i * i
    scat_num = min_value // mul_num
    if min_value % mul_num != 0:
        scat_num += 1
    while mul_num * scat_num <= max_value:
        numbers[(mul_num * scat_num) - min_value] = 0
        scat_num += 1    

print(sum(numbers))
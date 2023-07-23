"""
author: kyungmin
date: 23.07.23
title: 소수&팰린드롬
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

def search_prime_number(number):
    if number == 1:
        return False
    for i in range(2, int(number**.5) + 1):
        if number % i == 0:
            return False
    
    return True

num = N


while True:
    flag = 0
    if search_prime_number(num):
        str_num = str(num)
        start = 0
        end = len(str_num)-1
        while start < end:
            if str_num[start] == str_num[end]:
                start += 1
                end -= 1
            else:
                flag = 1
                break
    else:
        num += 1
        continue

    if flag == 0 :
        print(num)
        break
    else:
        num += 1
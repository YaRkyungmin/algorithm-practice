"""
author: kyungmin
date: 23.06.12
title: 평균 구하기
time: 20분
"""
n = int(input())

a = list(map(int, input().split()))
sum = 0
m = max(a)
for i in a :
    sum += i/m * 100

print(sum/n)
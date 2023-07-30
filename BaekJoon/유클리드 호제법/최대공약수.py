"""
author: kyungmin
date: 23.07.31
title: 최대공약수
time: 30분
"""
import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

def GCD(a, b):
    if a % b == 0:
        return b 
    else:
        return GCD(b, a%b)

print("1" * GCD(A, B))


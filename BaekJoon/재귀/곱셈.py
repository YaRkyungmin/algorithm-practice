"""
author: kyungmin
date: 23.12.12
title: 곱셈
time: 30분
"""
import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

def recursive(a, b, c):
    if b == 0:
        return 1
    
    tmp = recursive(a, b//2, c) % C
    tmp = (tmp * tmp) % c

    if b % 2 == 0:
        return tmp
    else:
        return (tmp * a) % c
    
print(recursive(A, B, C))
"""
author: kyungmin
date: 23.07.27
title: 최소공배수
time: 30분
"""
import sys
input = sys.stdin.readline

def GD(a, b):
    if a % b == 0:
        return b   
    else:
        test = GD(b, a % b)
    return test 

T = int(input().rstrip())
for _ in range(T):
    a, b = map(int, input().rstrip().split())
    if a < b:
        a, b = b, a
    common = GD(a, b)
    print(int(a / common) * b)

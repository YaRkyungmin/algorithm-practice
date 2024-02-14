"""
author: kyungmin
date: 24.2.15
title: 돌 게임
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

if N < 4:
    print("SK")
else:
    print("CY" if N % 4 == 0 else "SK")
        
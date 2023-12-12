"""
author: kyungmin
date: 23.12.12
title: 곱셈
time: 30분
"""
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

def recursive(cnt, total):
    if cnt == B:
        return total % C
    return recursive(cnt + 1, (total * A) % C)

print(recursive(0, 1))
"""
author: kyungmin
date: 23.07.18
title: 수 정렬하기 2
time: 30분
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
numbers = [int(input()) for _ in range(N)]

def merge_sort(S,E):
    if E - S < 1: return
    M = int(S + (E - S) / 2)
    merge_sort(S, M)
    merge_sort(M + 1, E)
    for i in range(S, E + 1):
        # tmp[i] = A[i]
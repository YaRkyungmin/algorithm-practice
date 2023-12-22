"""
author: kyungmin
date: 23.12.22
title: N과 M (1)
time: 30분
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
def sequence(m, partial):
    global N
    if m == 1:
        for i in range(1, N + 1):
            if i not in partial:
                partial.append(i)
        return partial
    arr = []
    for i in range(1, N + 1):
        arr.append(sequence(m - 1))
        partial.append(arr)

    return partial

print(sequence(M, []))
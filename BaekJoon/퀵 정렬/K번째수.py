"""
author: kyungmin
date: 23.07.15
title: K번째수
time: 30분
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
K -= 1

def quick_sort(S, E):
    pivot = get_pivot(S, E)

    if pivot == K:
        return numbers[pivot]
    elif pivot > K:
        quick_sort(S, pivot-1)
    else:
        quick_sort(pivot+1, E)

def swap(A, B):
    numbers[A], numbers[B] = numbers[B], numbers[A]

# 2 1 8 [3] 2 7 5 4
# 0 1 2 3 4 5 6 7

# 3 1 2 2 8 7 5 4

def get_pivot(S, E):
    M = S + E // 2

    swap(S, M)

    start = S + 1
    end = E
    while start <= end:
        while numbers[start] < numbers[S] and start <= end:
            start += 1
        while numbers[end] >= numbers[S] and start <= end:
            end -= 1
    
        if start < end:
            swap(start, end)
            start += 1
            end -= 1
    if end < start:
        swap(S, end)
        return end
    else:
        swap(S, start)
        return start


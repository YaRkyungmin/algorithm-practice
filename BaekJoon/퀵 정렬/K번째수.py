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
K -= 1
numbers = list(map(int, input().rstrip().split()))

def quickSort(S, E):
    if S < E:
        pivot = partition(S, E)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(S, pivot - 1)
        else:
            quickSort(pivot + 1, E)
    return

def swap(i, j):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp

# 4 7 2 3 1
# 2 7 4 3 1
#0 4
def partition(S, E):
    if S + 1 == E:
        if numbers[S] > numbers[E]:
            swap(S, E)
        return E
#2
    M = (S + E) // 2
    swap(S, M)
    pivot = numbers[S]
    i = S + 1
    j = E

#i = 1, j= 4
    while i <= j:
        while pivot < numbers[j] and j > 0:
            j = j - 1
        while pivot > numbers[i] and i < N - 1:
            i = i + 1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1

    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    swap(S, j)
    return j

quickSort(0, N - 1)
print(numbers[K])
    

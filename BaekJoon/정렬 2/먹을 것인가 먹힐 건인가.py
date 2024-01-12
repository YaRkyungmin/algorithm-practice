"""
author: kyungmin
date: 24.1.12
title: 먹을 것인가 먹힐 것인가
time: 30분
"""
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N, M = map(int, input().rstrip().split())
    a_list = list(map(int, input().rstrip().split()))
    b_list = list(map(int, input().rstrip().split()))

    a_list.sort()
    b_list.sort()
    pointer = 0
    sum = 0
    for i in a_list:
        while pointer < M and i > b_list[pointer]:
            pointer += 1
        sum += pointer
    print(sum)

"""
author: kyungmin
date: 23.06.22
title: 절댓값 힙
time: 30분
"""
import heapq
N = int(input())
arr = []
r = []
# for i in range(N):
#     inputValue = int(input())
#     sign = 0
#     if inputValue < 0:
#         inputValue = abs(inputValue)
#         sign = 1
        
#     if inputValue != 0: 
#         arr.append((inputValue,sign))
#     else:
#         if len(arr)
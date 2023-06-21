"""
author: kyungmin
date: 23.06.21
title: 카드2
time: 15분
"""
# from collections import deque
# N = int(input())
# d = deque()
# n = N+1
# while n > 1:
#     n -= 1
#     d.append(n)
# while len(d) > 1:
#     d.pop()
#     d.appendleft(d.pop())

# print(d.pop())

import sys
input=sys.stdin.readline
n=int(input())
def card(n):
    if n==1:
        return 1
    elif n%2==0:
        return 2*card(n/2)
    else:
        return 2*card((n+1)/2)-2
print(card(n))
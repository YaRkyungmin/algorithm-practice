"""
author: kyungmin
date: 23.12.14
title: Z
time: 30분
"""

import sys
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())

cnt = 0
def z_search(n, x, y):
    global cnt

    if x == c and y == r:   
        return
    
    pn = 2**(n-1)

    # 1사분면
    if x <= c < x + pn\
    and y <= r < y + pn:
        z_search(n - 1, x, y)
        return
    cnt += 2**(2*n-2)

    # 2사분면
    if x + pn <= c\
    and y <= r < y + pn:
        z_search(n - 1, x + pn, y)
        return
    cnt += 2**(2*n-2)

    # 3사분면
    if x <= c < x + pn\
    and y + pn <= r:
        z_search(n - 1, x, y + pn)
        return
    cnt += 2**(2*n-2)

    # 4사분면
    if x + pn <= c\
    and y + pn <= r:
        z_search(n - 1, x + pn, y + pn)
        return
    cnt += 2**(2*n-2)

z_search(N, 0, 0)

print(int(cnt))
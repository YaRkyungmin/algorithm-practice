"""
author: kyungmin
date: 23.12.22
title: N-Queen
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
is_ok = [[True] * N for _ in range(N)]

def combination1():
    global N, is_ok
    cnt = 0
    check_set = set()
    for dy in range(N):
        for dx in range(N):
            setup_checked(check_set)
            check1(dx, dy)
            check2(dx, dy)
            cnt += find_true()

            is_ok = [[True] * N for _ in range(N)]
            check_set.add((dx, dy))
    return cnt

def setup_checked(n):
    for x, y in n:
        is_ok[y][x] = False

def check1(x, y):
    global N
    for cx in range(N):
        is_ok[y][cx] = False
    for cy in range(N):
        is_ok[cy][x] = False
def check2(x, y):
    global N
    cx = x
    cy = y
    while 0 <= cx and 0 <= cy:
        is_ok[cy][cx] = False
        cx -= 1
        cy -= 1
                
    cx = x
    cy = y
    while 0 <= cx and cy < N:
        is_ok[cy][cx] = False
        cx -= 1
        cy += 1

    cx = x
    cy = y
    while cx < N and cy < N:
        is_ok[cy][cx] = False
        cx += 1
        cy += 1

    cx = x
    cy = y
    while cx < N and 0 <= cy:
        is_ok[cy][cx] = False
        cx += 1
        cy -= 1

def find_true():
    global N
    cnt = 0
    for y in range(N):
        for x in range(N):
            cnt += 1 if is_ok[y][x] == True else 0
    
    return cnt

print(combination1())
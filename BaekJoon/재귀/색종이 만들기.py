"""
author: kyungmin
date: 23.12.17
title: 색종이 만들기
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
T = [list(map(int, input().rstrip().split())) for _ in range(N)]
answer = [0, 0]

def divide(x, y, n):
    j_node = T[y][x]
    if n == 1:
        answer[j_node] += 1
        return
    signal = False
    b_signal = False
    for dy in range(y, y + n):
        for dx in range(x, x + n):
            if T[dy][dx] != j_node:
                b_signal = True
                signal = True
                break
        if b_signal:
            break
    
    if signal:
        for dy in range(2):
            for dx in range(2):
                px = x + (n//2 * dx)
                py = y + (n//2 * dy)
                divide(px, py, n//2)
    else:
        answer[j_node] += 1
divide(0, 0, N)
print(*answer, sep="\n")
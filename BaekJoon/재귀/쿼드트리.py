"""
author: kyungmin
date: 23.12.18
title: 쿼드트리
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
T = [list(input().rstrip()) for _ in range(N)]
def quad(x, y, n):
    q_node = T[y][x]
    if n == 1:
        return q_node
    
    b_signal = False
    signal = False

    for dy in range(y, y + n):
        for dx in range(x, x + n):
            if T[dy][dx] != q_node:
                b_signal = True
                signal = True
                break
        if b_signal:
            break

    if signal:
        output = []
        for dy in range(2):
            for dx in range(2):
                px = x + n//2 * dx
                py = y + n//2 * dy
                output.append(quad(px, py, n//2))
        return f"({output[0]}{output[1]}{output[2]}{output[3]})"
    else:
        return q_node

print(quad(0, 0, N))

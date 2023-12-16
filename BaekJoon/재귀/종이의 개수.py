"""
author: kyungmin
date: 23.12.16
title: 종이의 개수
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
T = [list(map(int, input().rstrip().split())) for _ in range(N)]
color = [0, 0, 0]
def nine(x, y, n):
    if n == 1:
        color[T[y][x]] += 1
        return
    signal = False
    j_node = T[y][x]
    for dy in range(y, y + n):
        y_signal = False
        for dx in range(x, x + n):
            if j_node != T[dy][dx]:
                signal = True
                y_signal = True
                break
        if y_signal:
            break         

    if signal: # 다른 노드 존재 할 때
        tn = n//3
        for iy in range(3):
            for ix in range(3):
                nine(x + tn*ix, y + tn*iy, tn)
    else: # 존재 하지 않을 때
        color[T[y][x]] += 1

nine(0, 0, N)
print(color[-1])
print(color[0])
print(color[1])
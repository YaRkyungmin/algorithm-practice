"""
author: kyungmin
date: 24.5.9
title: 스티커 붙이기
time: 30분
"""
import sys
input = sys.stdin.readline

def check(px, py, a):
    y_len = len(a)
    x_len = len(a[0])
    for y in range(0, y_len):
        for x in range(0, x_len):
            if a[y][x] == 1:
                if board[y + py][x + px] == 0:
                    continue
                else:
                    return False
    return True

def mark(px, py, a):
    y_len = len(a)
    x_len = len(a[0])
    for y in range(0, y_len):
        for x in range(0, x_len):
            if a[y][x] == 1:
                board[y + py][x + px] = 1

def total_check(a):
    global N, M
    y_len = len(a)
    x_len = len(a[0])

    for py in range(0, N - y_len + 1):
        for px in range(0, M - x_len + 1):
            if check(px, py, a):
                mark(px, py, a)
                return True
    return False

def turn_around(stic):
    y_len = len(stic)
    x_len = len(stic[0])
    turn_sticker = []
    for y in range(x_len):
        x_sticker = []
        for x in range(y_len - 1, -1, -1):
            x_sticker.append(stic[x][y])
        turn_sticker.append(x_sticker)
    return turn_sticker

def count_board():
    count = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                count += 1
    return count

N, M, K = map(int, input().rstrip().split())
# 세로, 가로, 스터커 수
board = [[0] * M for _ in range(N)]
sticker = []

for _ in range(K):
    n, m = map(int, input().rstrip().split())
    sticker.append([list(map(int, input().rstrip().split())) for _ in range(n)])

for i in range(K):
    attach = sticker[i]
    for _ in range(4):
        if total_check(attach):
            break
        attach = turn_around(attach)

print(count_board())
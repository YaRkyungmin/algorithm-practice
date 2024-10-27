"""
author: kyungmin
date: 24.9.25
title: 주사위 굴리기
time: 90분
"""
# score와 graph로 구현을 해아한다. 다른 방법으로는 코드가 굉장히 복잡해진다.

import sys
input = sys.stdin.readline

score = [0, 2, 4, 6, 8, 10, 12, 14,\
         16, 18, 20, 22, 24, 26, 28,\
         30, 32, 34, 36, 38, 40, 13,\
         16, 19, 22, 24, 28, 27, 26,\
         25, 30, 35, 0]

graph = [[1], [2], [3], [4], [5], [6, 21],\
         [7], [8], [9], [10], [11, 24],\
         [12], [13], [14], [15], [16, 26],\
         [17], [18], [19], [20], [32],\
         [22], [23], [29],\
         [25], [29],\
         [27], [28], [29],\
         [30], [31], [20]]

horse = [0 for _ in range(4)]
dices = list(map(int, input().rstrip().split()))
answer = 0

def move(h, s, m):
    tmp = horse[h]
    for i in range(s):
        if i == 0 and len(graph[tmp]) > 1: # 첫 시작이고 분기점에 있을 때
            tmp = graph[tmp][1]
        else: # 첫 시작이고 분기점이 아니거나 이동중 일때
            tmp = graph[tmp][0]
    
            if tmp == 32:
                horse[h] = -1 # 도착 처리
                return (True, m)

    if tmp in horse:
        return (False, m)
    else:
        horse[h] = tmp
        return (True, m + score[tmp])           

def play(step, point):
    global answer
    if step == 10:
        answer = max(point, answer)
        return

    for i in range(4):
        tmp = horse[i]

        if tmp == -1: # 이미 도착한 말일 때
            continue

        signal, m_point = move(i, dices[step], point)
        if signal:
            play(step + 1, m_point)
        else:
            continue
        horse[i] = tmp

play(0, 0)
print(answer)

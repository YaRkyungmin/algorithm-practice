"""
author: kyungmin
date: 23.12.22
title: N-Queen
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
is_ok_1 = [[True] for _ in range(N)] # y축
is_ok_3 = [[True] for _ in range(N * 2 - 1)] # 슬래쉬 /
is_ok_4 = [[True] for _ in range(N * 2 - 1)] # 역슬래쉬 \
cnt = 0

def combination(k):
    global N, cnt
    if k == N:
        cnt += 1
        return
    
    for dx in range(N):
        if is_ok_1[dx]\
        and is_ok_3[k + dx]\
        and is_ok_4[k - dx]:
            
            is_ok_1[dx] = False
            is_ok_3[k + dx] = False
            is_ok_4[k - dx] = False
            combination(k + 1)
            is_ok_1[dx] = True
            is_ok_3[k + dx] = True
            is_ok_4[k - dx] = True
        
combination(0)
print(cnt)
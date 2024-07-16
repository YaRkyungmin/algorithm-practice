"""
author: kyungmin
date: 24.07.17
title: 뒤집기
time: 30분
"""
import sys
input = sys.stdin.readline

card = input().rstrip()
pick = card[0]
cnt = 0
for i in range(len(card)):
    if pick != card[i]:
        cnt += 1
        pick = card[i]
print(cnt//2 + 1 if cnt%2 == 1 else cnt//2)
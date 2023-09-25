"""
author: kyungmin
date: 23.09.28
title: 피로도
time: 30분
"""

import sys
sys.setrecursionlimit(1500000)

answer = 0

def solution(k, dungeons):
    for i in range(len(dungeons)):
        dungeon_in(k, dungeons[i], dungeons[:i] + dungeons[i + 1:len(dungeons)], 0)
        
    return answer

def dungeon_in(k, dungeon, dungeons, count):
    global answer
    
    if k < dungeon[0]:
        if count > answer:
            answer = count
    
    if len(dungeons) == 0:
        count += 1
        if count > answer:
            answer = count
    
    for i in range(len(dungeons)):
        dungeon_in(k - dungeon[1], dungeons[i], dungeons[:i] + dungeons[i + 1:len(dungeons)], count + 1)
    
    return

print(solution(80, [[80,20],[50,40],[30,10]]))
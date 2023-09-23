"""
author: kyungmin
date: 23.09.26
title: 등굣길
time: 30분
"""

def solution(m, n, puddles):
    map = [[100] * m for i in range(n)]
    for i in range(n):
        map[i][0] = 1
    for i in range(m):
        map[0][i] = 1
        
    for puddle in puddles:
        if puddle[1] == 1:
            for i in range(puddle[0] - 1, m):
                map[0][i] = 0
        elif puddle[0] == 1:
            for i in range(puddle[1] - 1, n):
                map[i][0] = 0
        else :
            map[puddle[1] - 1][puddle[0] - 1] = 0
        
    
    for y in range(1,n):
        for x in range(1,m):
            if map[y][x] == 0:
                continue
                
            map[y][x] = map[y][x-1] + map[y-1][x]
            
                    
    answer = map[n-1][m-1] % 1000000007
    return answer
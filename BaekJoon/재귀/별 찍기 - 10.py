"""
author: kyungmin
date: 23.12.19
title: 별 찍기 - 10
time: 30분
"""
import sys
input = sys.stdin.readline
N = int(input().rstrip())

def star(n):
    if n == 3:
        star_st = ""
        for y in range(n):
            for x in range(n):
                if x == 1 and y == 1:
                    star_st += " "
                else:
                    star_st += "*"
            if y == 0 or y == 1:
                star_st += "\n"
        return star_st
    
    m_star = star(n//3).split("\n")
    d1 = ""
    for i in range(len(m_star)):
        if i == len(m_star) -1:
            d1 += (m_star[i] * 3) 
        else:
            d1 += (m_star[i] * 3) + "\n"
    d2 = "\n"
    for i in range(len(m_star)):
        d2 += m_star[i] + (" " * (n//3)) + m_star[i] + "\n"
    
    return d1 + d2 + d1

print(star(N))
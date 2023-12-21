"""
author: kyungmin
date: 23.12.21
title: 별 찍기 - 11
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

def tri_star(n):
    k = n//3
    star_st = ""
    if k == 1:
        s_star  = ["  *  ", " * * ", "*****"]
        return "\n".join(s_star)
    tri_arr = tri_star(n//2).split("\n")
    space = " " * (n//2)
    b1_tri_arr = []
    b2_tri_arr = []
    for tri in tri_arr:
        b1_tri_arr.append(space + tri + space)
        b2_tri_arr.append(tri + " " + tri)
    return "\n".join(b1_tri_arr + b2_tri_arr)
print(tri_star(N))
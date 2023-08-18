"""
author: kyungmin
date: 23.08.18
title: 여행가자
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip()) 
parents = [i for i in range(N+1)]

def union(a, b):
    parents[find(b)] = find(a)
    
def find(x):
    while parents[x] != x:
        x = parents[x]    
    return x

city = [list(map(int, input().rstrip().split())) for _ in range(N)]

for x in range(N):
    for y in range(N):
        if city[x][y] == 1:
            if x > y:
                union(x+1,y+1)

map = list(map(int, input().rstrip().split()))

result = 0

for i in range(M-1):
    if find(map[i]) != find(map[i+1]):
        result = 1
        break
           
if result == 0:
    print("YES")
else:
    print("NO")


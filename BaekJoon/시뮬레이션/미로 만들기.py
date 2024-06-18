"""
author: kyungmin
date: 24.6.18
title: 미로 만들기
time: 30분
"""
import sys
input = sys.stdin.readline

def turnRight(index):
    if index == 3:
        return 0
    else:
        return index + 1
def turnLeft(index):
    if index == 0:
        return 3
    else:
        return index -1

N = input()
road = input().rstrip()

road_map = [["#" for _ in range(102)] for _ in range(102)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
p = 0
px = 50
py = 50

min_x = px
min_y = py
max_x = px
max_y = py

def updateData(x, y):
    global min_x, min_y, max_x, max_y
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_x = max(x, max_x)
    max_y = max(y, max_y)
road_map[py][px] = "."
    
for i in road:
    if i == "R":
        p = turnRight(p)
    elif i == "L":
        p = turnLeft(p)        
    else:
        px += dx[p]
        py += dy[p]
        updateData(px, py)
        road_map[py][px] = "."

for y in range(min_y, max_y + 1):
    result = road_map[y][min_x:max_x + 1]
    print("".join(result))

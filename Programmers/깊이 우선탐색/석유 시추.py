"""
author: kyungmin
date: 24.08.04
title: 석유 시추
time: 30분
"""
index = 1
x = 0
y = 0
answer = 0
def solution(land):
    global x, y, answer
    y = len(land)
    x = len(land[0])
    visit = [[0] * x for _ in range(y)]
    
    dp = [0 for _ in range((x * y)//2 + 1)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    def dfs(ix, iy):
        global index, x, y
        count = 1
        stack = [(ix, iy)]
        visit[iy][ix] = index
        while stack:
            px, py = stack.pop()
            for i in range(4):
                cx = px + dx[i]
                cy = py + dy[i]
                if 0 <= cy < y\
                and 0 <= cx < x\
                and land[cy][cx] == 1\
                and visit[cy][cx] == 0:
                    stack.append((cx, cy))
                    visit[cy][cx] = index
                    count += 1
        dp[index] = count
        index += 1
        
    for py in range(y):
        for px in range(x):
            if land[py][px] == 1\
            and visit[py][px] == 0:
                dfs(px, py)
    
    def suck():
        global x, y, answer
        for px in range(x):
            count = 0
            land_set = set()
            for py in range(y):
                land_set.add(visit[py][px])
            for i in land_set:
                count += dp[i]
            answer = max(answer, count)
    suck()
    
    return answer
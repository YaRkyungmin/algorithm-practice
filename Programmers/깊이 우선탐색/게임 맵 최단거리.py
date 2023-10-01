"""
author: kyungmin
date: 23.10.02
title: 게임 맵 최단거리
time: 30분
"""

from copy import deepcopy

end_x = 0
end_y = 0
answer = -1

def solution(maps):
    global end_x, end_y, answer
    
    end_x = len(maps[0]) - 1
    end_y = len(maps) - 1
    
    dfs(1, maps, 0, 0)

    return answer

def dfs(count, game_map, x, y):
    global end_x, end_y, answer

    if x == end_x and y == end_y:
        if answer != -1 and answer > count:
            answer = count
            return
        elif answer == -1:
            answer = count
            return

    E = [x + 1, y]
    W = [x - 1, y]
    N = [x, y - 1]
    S = [x, y + 1]
    
    lili = [E,W,S,N]
    new_map = deepcopy(game_map)


    for li in lili:
        if li[0] >= 0 and li[0] <= end_x and li[1] >= 0 and li[1] <= end_y:
            if new_map[li[1]][li[0]] == 1:
                count += 1
                new_map[y][x] = 0
                dfs(count, new_map, li[0], li[1])
    
    return
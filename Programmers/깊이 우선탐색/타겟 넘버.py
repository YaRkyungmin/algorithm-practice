"""
author: kyungmin
date: 23.09.05
title: 타겟 넘버
time: 30분
"""



def solution(numbers, target):
    count = 0
    visited = [0] * len(numbers)
    visit = []
    max_depth = len(numbers)
    stack = [[numbers[0], 1], [-numbers[0], 1]]
    while stack:
        [node, depth] = stack.pop()
        if depth < max_depth:
            if visit:
                if visit[-1][1] == depth:
                    visit.pop()
                    visited[depth] += 1
            visit.append([node, depth])
            stack.append([[numbers[depth], depth + 1], [-numbers[depth], depth +1]])
        else:
            visit.append([node, depth])
            sum = 0
            for i in range(max_depth):
                sum += visit[i][0]

            if sum == target:
                count += 1

            visit.pop()
    return count 


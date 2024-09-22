"""
author: kyungmin
date: 23.09.08
title: 섬 연결하기
time: 30분
"""
from heapq import *
def solution(n, costs):
    for i in range(len(costs)):
        costs[i] = [costs[i][2], costs[i][0], costs[i][1]]
    visit = [True for _ in range(n)]
    if len(costs) == 1:
        return 0
    count = 2
    heapify(costs)
    S, a, b = heappop(costs)
    visit[a] = False
    visit[b] = False
    answer = S

    while count < n:
        stack = []
        signal = True
        while signal:
            S, a, b = heappop(costs)
            if visit[a] and visit[b] == False:
                signal = False        
                count += 1
                answer += S
                visit[a] = False
            elif  visit[b] and visit[a] == False:
                signal = False
                count += 1
                answer += S
                visit[b] = False
            if signal:
                stack.append([S, a, b])
        while stack:
            heappush(costs, stack.pop())

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,1],[1,3,1],[2,3,8]]))
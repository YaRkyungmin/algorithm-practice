"""
author: kyungmin
date: 23.09.19
title: 여행경로
time: 30분
"""

from collections import defaultdict


def solution(tickets):
    answer = []
    adj = defaultdict(list)

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    for key in adj.keys():
        adj[key].sort(reverse=True)

    q = ['ICN']
    while q:
        tmp = q[-1]

        if not adj[tmp]:
            answer.append(q.pop())
        else:
            q.append(adj[tmp].pop())
    answer.reverse()
    return answer

result = solution([['ICN','A'],['A','B'],['A','C'],['C','A'],['B','D']])

print(result)


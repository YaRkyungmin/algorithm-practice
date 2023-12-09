"""
author: kyungmin
date: 23.12.08
title: 텀 프로젝트
time: 30분
"""
## 사이클을 찾아보는 의미 있는 문제 였음
import sys
input = sys.stdin.readline
from collections import deque
T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    members = list(map(int, input().rstrip().split()))
    queue = deque()
    visit = [False for _ in range(n+1)]
    solos = [False for _ in range(n+1)]
    for i in range(1, n + 1):
        if visit[i]:
            continue
        queue.append(i)
        p_visit = []
        while queue:
            node = queue.pop()
            visit[node] = True
            p_visit.append(node)
            if visit[members[node - 1]] == False: #방문 안 했을때
                queue.append(members[node - 1])
            else: # 방문 했을때
                for xx in p_visit:
                    if xx == members[node - 1]: #사이클 시작점 찾기
                        break
                    solos[xx] = True
    
    print(solos.count(True))
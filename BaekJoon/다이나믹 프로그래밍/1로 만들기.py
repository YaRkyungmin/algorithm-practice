"""
author: kyungmin
date: 23.12.16
title: 1로 만들기
time: 30분
"""
import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())

visit = set()
queue = deque()

queue.append((N, 0))
while queue:
    node, cnt = queue.popleft()
    if node == 1:
        print(cnt)
        break
    
    if node % 3 == 0 and node // 3 not in visit:
        queue.append((node // 3, cnt + 1))
        visit.add(node // 3)
    if node % 2 == 0 and node // 2 not in visit:
        queue.append((node // 2, cnt + 1))
        visit.add(node // 2)
    if node - 1 not in visit:
        queue.append((node - 1, cnt + 1))
        visit.add(node - 1)

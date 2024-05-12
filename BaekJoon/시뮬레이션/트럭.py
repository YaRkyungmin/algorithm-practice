"""
author: kyungmin
date: 24.5.9
title: 트럭
time: 30분
"""
# n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중
from collections import deque

N, W, L = map(int, input().rstrip().split())
trucks = deque(list(map(int, input().rstrip().split())))
leg = [0 for i in range(W)]
time = 0
total_weight = 0
        
def move_truck():
    global leg, total_weight
    for i in range(len(leg)):
        if i == 0:
            total_weight -= leg[i]
        if i != 0:
            leg[i - 1] = leg[i]
        leg[i] = 0

while trucks or total_weight > 0:
    time += 1
    move_truck()
    if trucks:
        if L - total_weight >= trucks[0]:
            t = trucks.popleft()
            leg[W - 1] = t
            total_weight += t
    
print(time)



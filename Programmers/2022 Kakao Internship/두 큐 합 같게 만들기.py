"""
author: kyungmin
date: 23.11.10
title: 두 큐 합 같게 만들기
time: 30분
"""
from collections import deque

def solution(queue1, queue2):
    queue_one = deque(queue1)
    queue_two = deque(queue2)
    max_result = 3 * len(queue1)
    result = 0
    
    sum1 = sum(queue_one)
    sum2 = sum(queue_two)
    
    while sum1 != sum2:
        if result == max_result:
            result = -1
            break
            
        if sum1 > sum2:
            pop_ele = queue_one.popleft()
            sum1 -= pop_ele
            sum2 += pop_ele
            queue_two.append(pop_ele)
            result += 1
        else:
            pop_ele = queue_two.popleft()
            sum2 -= pop_ele
            sum1 += pop_ele
            queue_one.append(pop_ele)
            result += 1
    
    return result

print(solution([1,1,1,1,1],[1,1,1,9,1]))
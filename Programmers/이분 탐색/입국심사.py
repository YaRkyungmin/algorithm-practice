"""
author: kyungmin
date: 23.09.14
title: 입국심사
time: 30분
"""
def solution(n, times):
    times.sort()
    min_time = times[0]
    x = 0
    times_len = len(times)
    time_set = [0] * times_len
    while n >= sum(time_set):
        x += 1
        compare_time = min_time * x
        for i in range(times_len):
            if times[i] <= compare_time:
                time_set[i] += 1
            else:
                break
    y = 0
    while sum(time_set) > n:
        time_set[y] -= 1
        y += 1
    
    z = times_len - 1
    
    total_time = time_set[0] * times[0]
    
    for i in range(1, times_len):
        if time_set[i] == 0:
            break
        if total_time < time_set[i] * times[i]:
            total_time = time_set[i] * times[i]
    
    return total_time
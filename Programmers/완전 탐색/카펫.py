"""
author: kyungmin
date: 23.09.13
title: 카펫
time: 30분
"""

def solution(brown, yellow):
    answer = []
    kaffet_count = brown + yellow
    array_list = []
    for i in range(1, int(kaffet_count**.5) + 1):
        if kaffet_count % i == 0:
            a = kaffet_count // i
            b = i
            if a < b:
                tmp = a
                a = b
                b = tmp
            array_list.append([a, b])
    while array_list:
        [a, b] = array_list.pop()
        if (a-2) * (b-2) == yellow:
            answer = [a, b]
            break       
    return answer
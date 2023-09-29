"""
author: kyungmin
date: 23.10.01
title: N으로 표현
time: 30분
"""

dp = []

def solution(N, number):
    for i in range(1,9):
        append_case = configure_list(N, i)
        
        if number in append_case:
            return i
        else:
            dp.append(append_case)
    
    return -1
    
    
def configure_list(N, cnt):
    all_case = set()
    all_case.add(int(str(N) * cnt))
    
    for i in range(1, cnt):
        for dp1 in dp[i - 1]:
            for dp2 in dp[cnt - i - 1]:
                all_case.add(dp1 + dp2)
                all_case.add(dp1 - dp2)
                all_case.add(dp1 * dp2)
                if dp1 != 0 and dp2 != 0:
                    all_case.add(dp1 // dp2)
    
    return all_case
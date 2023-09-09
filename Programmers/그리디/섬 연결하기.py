"""
author: kyungmin
date: 23.09.08
title: 섬 연결하기
time: 30분
"""
def solution(n, costs):
    answer = 0
    dp = [False] * n
    costs.sort(key = lambda x: x[2]) 

    for i in costs:
        if dp[i[0]] and dp[i[1]]:
            continue
        dp[i[0]] = True
        dp[i[1]] = True
        answer += i[2]
    return answer
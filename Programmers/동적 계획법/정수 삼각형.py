"""
author: kyungmin
date: 23.09.06
title: 정수 삼각형
time: 30분
"""

def solution(triangle):
    dp = []
    top_level = len(triangle)
    for i in range(top_level):
        append_list = []
        for _ in range(0,i+1):
            append_list.append(0)
        dp.append(append_list)

    dp[0][0] = triangle[0][0]

    for i in range(1, top_level):
        level = len(dp[i])
        for x in range(level):
            if x == 0 :
                dp[i][x] = triangle[i][x] + dp[i-1][x]
            elif x == (level - 1):
                dp[i][x] = triangle[i][x] + dp[i-1][x-1]
            else:
                dp[i][x] = triangle[i][x] + max(dp[i-1][x],dp[i-1][x-1])

    return max(dp[top_level - 1])
    
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
    

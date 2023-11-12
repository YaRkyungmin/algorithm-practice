"""
author: kyungmin
date: 23.11.12
title: 성격 유형 검사하기
time: 30분
"""

def solution(alp, cop, problems):
    INF = float('inf')

    # dp 배열 초기화
    dp = [[INF] * (cop + 1) for _ in range(alp + 1)]
    dp[alp][cop] = 0  # 초기 상태는 주어진 알고력과 코딩력

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        for i in range(alp + 1):
            for j in range(cop + 1):
                # 현재 상태에서 문제를 풀 수 있는지 확인
                if i >= alp_req and j >= cop_req:
                    # 현재 상태에서 문제를 푸는데 필요한 비용 계산
                    new_i = min(alp, i - alp_req + alp_rwd)
                    new_j = min(cop, j - cop_req + cop_rwd)
                    dp[new_i][new_j] = min(dp[new_i][new_j], dp[i][j] + cost)

    result = INF
    # 최종 결과는 모든 가능한 상태에서의 최소 비용
    for i in range(alp + 1):
        for j in range(cop + 1):
            result = min(result, dp[i][j])

    return result if result != INF else -1  # 모든 상태에서의 비용이 INF인 경우, 문제를 풀 수 없음을 나타냄

# 테스트 케이스
print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))  # 15
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))  # 13
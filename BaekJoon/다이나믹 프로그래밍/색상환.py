"""
author: kyungmin
date: 24.2.21
title: 색상환
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())


dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
dp[1][1] = 1

for n in range(2, N + 1):
    dp[n][1] = n    

    for k in range(2, K + 1):
        if k * 2 <= n:
            dp[n][k] = (dp[n - 1][k] + dp[n - 2][k - 1]) % 1000000003
        else:
            break

print(dp[N][K])

# 1. 2개의 작은 원으로 큰원을 만드는 방법
# 2. 하나의 큰원 안에서 선형 + 원형 갯수를 더하는 방법
# 2번째 경우로 다시 풀어보기
# https://source-sc.tistory.com/5
# https://ca.ramel.be/149
"""
author: kyungmin
date: 24.3.2
title: 구간 자르기
time: 30분
"""
import sys
input = sys.stdin.readline

# 구간 자르기 문제를 처리하는 방법(누적합)을 알 수 있는 문제
# 시작위치 +1, 종료위치 -1 해준뒤 모든위치를 순회하며 arr[i] += arr[i-1]
N, K = map(int, input().rstrip().split())
dp = [0 for _ in range(1000001)]

for _ in range(N):
    st, en = map(int, input().rstrip().split())
    dp[st] += 1
    dp[en] -= 1

for i in range(1, 1000001):
    dp[i] += dp[i - 1]
p_sum = 0
result = [0, 0]
st = 0
en = 0

while en <= 1000001:
    if p_sum < K:
        if en == 1000001:
            break
        p_sum += dp[en]
        en += 1
    elif p_sum > K:
        p_sum -= dp[st]
        st += 1
    else:
        result = [st, en]
        break

print(*result)
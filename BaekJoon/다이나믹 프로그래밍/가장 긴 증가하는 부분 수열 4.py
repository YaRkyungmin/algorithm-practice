"""
author: kyungmin
date: 24.2.1
title: 가장 긴 증가하는 부분 수열 4
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = [0] + list(map(int, input().rstrip().split()))
dp = [1 for _ in range(N + 1)]
history = [0 for _ in range(N + 1)]
result = 1
p = 1

for i in range(2, N + 1):
    for j in range(1, i):
        if numbers[i] > numbers[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            history[i] = j
            if result < dp[i]:
                result = dp[i]
                p = i

result_arr = []
while p != 0:
    result_arr.append(numbers[p])
    p = history[p]

print(result)
print(*result_arr[::-1])

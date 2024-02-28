"""
author: kyungmin
date: 24.2.28
title: 회전 초밥
time: 30분
"""
import sys
input = sys.stdin.readline

# N: 접시수, d: 가짓수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호
# set으로 구현하지말고 set의 기능을 하도록 visited를 이용하면 시간을 줄일 수 있음 (review시 이 방식으로 구현 하기!)
N, d, k, c = map(int, input().rstrip().split())
numbers = [int(input().rstrip()) for _ in range(N)]
p = 0
result = 0

while p < N:
    p_len = p + k
    p_set = set()
    if p_len <= N:
        p_set = set(numbers[p:p_len] + [c])
    else:
        p_set = set(numbers[p:N] + numbers[:p_len%N] + [c])
    p += 1   
    result = max(len(p_set), result)

print(result)

# #입력
# n, d, k, c= map(int, input().split())
# sushi = [int(input()) for _ in range(n)]


# #초기화
# visited = [0]*3001
# from collections import deque
# dq= deque([])
# count = 0
# result = 0

# #k개 까지 채워본 후 갯수 세보기
# for i in range(k):
#     if visited[sushi[i]] == 0:
#         count += 1    
#     dq.append(sushi[i])
#     visited[sushi[i]] += 1
    
# if visited[c] == 0:
#     result = max(result, count + 1)
# else:
#     result = max(result, count)

# #k개 채운 이후부터 한 칸 씩 밀어가며 실행
# for i in range(k, n + k - 1):
#     left = dq.popleft()
#     if visited[left] > 0:
#         visited[left] -= 1
#         if visited[left] == 0:
#             count -= 1
    
#     idx = i % n
    
#     if visited[sushi[idx]] == 0:
#         count += 1
#     visited[sushi[idx]] += 1
#     dq.append(sushi[idx])

#     if visited[c] == 0:
#         result = max(result, count + 1)
#     else:
#         result = max(result, count)

    
    

# print(result)
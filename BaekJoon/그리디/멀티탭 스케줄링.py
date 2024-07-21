"""
author: kyungmin
date: 24.07.19
title: 멀티탭 스케줄링
time: 30분
"""
# 반례
# 3 100
# 56 71 70 25 52 77 76 8 68 71 51 65 13 23 7 16 19 54 95 18 86 74 29 76 61 93 44 96 32 72 64 19 50 49 22 14 7 64 24 83 6 3 2 76 99 7 76 100 60 60 6 50 90 49 27 51 37 61 16 84 89 51 73 28 90 77 73 39 78 96 78 13 92 54 70 69 62 78 7 75 30 67 97 98 19 86 90 90 2 39 41 58 57 84 19 8 52 39 26 7
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

con = []
elec = [-1 for _ in range(K + 1)]
cnt = 0

for i in range(K):
    next = 0 #다음에 나오는 값 정하기
    for x in range(i + 1, K):
        if nums[i] == nums[x]:
            next = x
            break

    if elec[nums[i]] == -1: #꽂혀있지 않을 때
        if len(con) < N: # 콘센트가 남아있을 때
            con.append(nums[i])
            elec[nums[i]] = next
        else: # 콘센트가 안남았을 때
            m = -1
            d = 0 ## 뺄 아이
            for x in range(N):
                if elec[con[x]] == 0:
                    d = x
                    break
                if elec[con[x]] > m:
                    d = x
                    m = elec[con[x]]
            cnt += 1
            elec[con[d]] = -1
            con[d] = nums[i]
            elec[nums[i]] = next

    else: #꽂혀있을 때
        elec[nums[i]] = next

print(cnt)
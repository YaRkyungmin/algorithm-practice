"""
author: kyungmin
date: 24.07.16
title: 공주님의 정원
time: 30분
"""
import sys
input = sys.stdin.readline

# 3월 1일부터 11월 30일까지

# 올해는 4, 6, 9, 11월은 30일까지 있고, 
# 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 
# 2월은 28일까지만 있다

N = int(input().rstrip())

all_date = [list(map(int, input().rstrip().split())) for _ in range(N)]
all_date.sort()

# 기준일
start_date = [3, 1]
c = 0
signal = True
idx = 0
while start_date[0] < 12 and signal:
    signal = False
    end_date = start_date.copy()
    for i in range(idx, N):
        if all_date[i][0] == start_date[0]\
        and all_date[i][1] <= start_date[1]\
        or all_date[i][0] < start_date[0]:
            if all_date[i][2] == end_date[0]\
            and all_date[i][3] > end_date[1]\
            or all_date[i][2] > end_date[0]:
                end_date[0] = all_date[i][2]
                end_date[1] = all_date[i][3]
                signal = True
                idx = i

    start_date[0] = end_date[0]
    start_date[1] = end_date[1]
    c += 1

print(c if signal else 0)


        




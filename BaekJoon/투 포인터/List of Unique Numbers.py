"""
author: kyungmin
date: 24.2.26
title: List of Unique Numbers
time: 30분
"""
import sys
input = sys.stdin.readline
N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

p_set = set()
st = 0
en = 0
result = 0

while en < N:
    if numbers[en] not in p_set:
        p_set.add(numbers[en])
        en += 1
    else:
        result += en - st
        p_set.remove(numbers[st])
        st += 1
n = en - st
result += int(n * (n + 1) * 1/2)
print(result)

# 연속된 수를 뽑는 경우의 수 는 n(n+1)*1/2 입니다
# https://connie.tistory.com/20
"""
author: kyungmin
date: 23.07.20
title: 수 정렬하기 3
time: 30분
"""
# from collections import deque
# import sys
# input = sys.stdin.readline

# numbers_queue = [deque() for _ in range(10)]

# N = int(input().rstrip())
# numbers = [int(input().rstrip()) for _ in range(N)]

# max_number = max(numbers)
# M = 1

# if max_number == 10000:
#     M = 5
# elif 1000 <= max_number <= 9999:
#     M = 4
# elif 100 <= max_number <= 999:
#     M = 3
# elif 10 <= max_number <= 99:
#     M = 2
# else:
#     M = 1

# for i in range(1, M+1):
#     for element in numbers:
#         numbers_queue[(element % (10**i)) // (10**(i-1))].append(element)
#     numbers = []
#     for queue in numbers_queue:
#         while queue:
#             numbers.append(queue.popleft())

# print(*numbers, sep="\n")


# import heapq
# import sys
# input = sys.stdin.readline

# numbers = [int(input().rstrip()) for _ in range(int(input().rstrip()))]
# numbers.sort()

# print(*numbers, sep="\n")

# for _ in range(int(input().rstrip())):
#     heapq.heappush(numbers, int(input().rstrip()))

# while numbers:
#     print(heapq.heappop(numbers))

import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = [0] * 10001

for _ in range(N):
    numbers[int(input().rstrip())] += 1

for i in range(10001):
    while numbers[i] > 0 :
        print(i)
        numbers[i] -= 1
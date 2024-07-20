"""
author: kyungmin
date: 24.07.20
title: 큰 수 만들기
time: 30분
"""
## O(n^2) 인 시간 복잡도 
# def solution(number, k):
#     l = len(number)
#     answer = ""
#     pick = -1
#     for i in range(l - k, 0, -1):
#         m = "0"
#         for x in range(pick + 1, l - i + 1):
#             num = number[x]
#             if num > m:
#                 pick = x
#                 m = num
#         answer += m
#         if pick == l - i:
#             for x in range(pick + 1, l):
#                 answer += number[x]
#             return answer
        
#     return answer

## O(2n) 인 시간 복잡도 , 반례 "93939" k = 3 일 때
def solution(number, k):
    stack = []
    for i in number:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)

    stack = stack[:len(stack) - k]        
        
    return "".join(stack)
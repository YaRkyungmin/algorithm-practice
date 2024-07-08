"""
author: kyungmin
date: 24.07.08
title: 괄호의 값
time: 30분
"""
import sys
input = sys.stdin.readline
result = 0
stack = []
for i in input().rstrip():
    if i == "(":
        stack.append(["(", 0])
    elif i == "[":
        stack.append(["[", 0])
    elif i == ")":
        if stack and stack[-1][0] == "(":
            pop_li = stack.pop()
            if pop_li[1] == 0:
                if stack:
                    stack[-1][1] += 2
                else:
                    result += 2
            else:
                if stack:
                    stack[-1][1] += 2 * pop_li[1]
                else:
                    result += 2 * pop_li[1]
        else:
            result = 0
            break
    elif i == "]":
        if stack and stack[-1][0] == "[":
            pop_li = stack.pop()
            if pop_li[1] == 0:
                if stack:
                    stack[-1][1] += 3
                else:
                    result += 3
            else:
                if stack:
                    stack[-1][1] += 3 * pop_li[1]
                else:
                    result += 3 * pop_li[1]

        else:
            result = 0
            break
    else:
        result = 0
        break

print(result)
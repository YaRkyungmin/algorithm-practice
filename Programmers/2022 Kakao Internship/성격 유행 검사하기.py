"""
author: kyungmin
date: 23.11.08
title: 성격 유형 검사하기
time: 30분
"""

R = 0
T = 0
C = 0
F = 0
J = 0
M = 0
A = 0
N = 0

def solution(survey, choices):
    global R, T, C, F, J, M, A, N
    
    for i in range(0, len(survey)):
        if choices[i] == 1:
            plusPoint(survey[i][0],3)
        elif choices[i] == 2:
            plusPoint(survey[i][0],2)
        elif choices[i] == 3:
            plusPoint(survey[i][0],1)
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            plusPoint(survey[i][1],1)
        elif choices[i] == 6:
            plusPoint(survey[i][1],2)
        else:
            plusPoint(survey[i][1],3)
    result = ""
    if R >= T:
        result += "R"
    else:
        result += "T"
    if C >= F:
        result += "C"
    else:
        result += "F"
    if J >= M:
        result += "J"
    else:
        result += "M"
    if A >= N:
        result += "A"
    else:
        result += "N"
        
    return result

def plusPoint(what, point):
    global R, T, C, F, J, M, A, N
    
    if what == "R":
        R += point
    elif what == "T":
        T += point
    elif what == "C":
        C += point
    elif what == "F":
        F += point
    elif what == "J":
        J += point
    elif what == "M":
        M += point
    elif what == "A":
        A += point
    else:
        N += point    
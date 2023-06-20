"""
author: kyungmin
date: 23.06.18
title: DNA 비밀번호
time: 30분
"""
S, P = map(int, input().split())
inputString = input()
condition = list(map(int, input().split()))
slideCount = [0 for i in range(4)]
result = 0
p = P - 1 

def countACGT(chracter):
    if chracter == "A":
        return 0
    elif chracter == "C":
        return 1
    elif chracter == "G":
        return 2
    else:
        return 3

def checkPassWord():
    if condition[0] <= slideCount[0] and condition[1] <= slideCount[1] and condition[2] <= slideCount[2] and condition[3] <= slideCount[3]:
        return True
    else:
        return False

for i in range(P):
    slideCount[countACGT(inputString[i])] += 1

while p < S:
    if checkPassWord():
        result += 1
    p += 1
    if p < S:
        slideCount[countACGT(inputString[p])] += 1
        slideCount[countACGT(inputString[p-P])] -= 1
print(result)
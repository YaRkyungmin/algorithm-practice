"""
author: kyungmin
date: 23.06.20
title: 스택 수열
time: 15분
"""
# 55분까지
# n = int(input())
# arr = [0 for i in range(n)]
# stack = []
# number = 0
# r = ""
# for i in range(n):
#     arr[i] = int(input())

# for i in arr:
#     while i > number: 
#         number += 1   
#         stack.append(number)
#         r += "+"
#     if stack.pop() == i:
#         r += "-"
#     else:
#         r = "NO"
#         break
# if r == "NO":
#     print(r)
# else:
#     for i in r:
#         print(i)

n = int(input())
arr = [0 for i in range(n)]
stack = []
number = 0
r = []
for i in range(n):
    arr[i] = int(input())

for i in arr:
    while i > number: 
        number += 1   
        stack.append(number)
        r.append("+")
    if stack.pop() == i:
        r.append("-")
    else:
        r = 0
        break
if r == 0:
    print("NO")
else:
    for i in r:
        print(i)
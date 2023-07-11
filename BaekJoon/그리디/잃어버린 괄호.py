"""
author: kyungmin
date: 23.07.11
title: 잃어버린 괄호
time: 30분
"""
expression = input()
result = 0
numbers = list(expression.split("-"))
if numbers[0] == "":
    # 맨앞이 음수 
    if len(numbers) >= 2:
        for i in range(1, len(numbers)):
            integers = list(map(int, numbers[i].split("+")))
            result -= sum(integers)
else:
    # 맨앞이 양수
    if len(numbers) >= 1: 
        integers = list(map(int, numbers[0].split("+")))
        result += sum(integers)
        for i in range(1,len(numbers)):
            integers = list(map(int, numbers[i].split("+")))
            result -= sum(integers)
print(result)

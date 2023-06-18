"""
author: kyungmin
date: 23.06.18
title: DNA 비밀번호
time: 30분
"""
S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())
p = P - 1
ac, cc, gc, tc = 0,0,0,0
count = 0
# [a c c c] c g t t a
for i in range(P):
    if DNA[i] == "A":
        ac += 1
    elif DNA[i] == "C":
        cc += 1
    elif DNA[i] == "G":
        gc += 1
    else :
        tc += 1
while p < S :
    if ac >= A and cc >= C and gc >= G and tc >= T:
        count += 1
    p += 1
    if p < S:
        if DNA[p] == "A":
            ac += 1
        elif DNA[p] == "C":
            cc += 1
        elif DNA[p] == "G":
            gc += 1
        else:
            tc += 1
        
        sub = p - P

        if DNA[sub] == "A":
            ac -= 1
        elif DNA[sub] == "C":
            cc -= 1
        elif DNA[sub] == "G":
            gc -= 1
        else:
            tc -= 1
print(count)
        
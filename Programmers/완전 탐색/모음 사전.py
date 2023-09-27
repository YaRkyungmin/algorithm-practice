"""
author: kyungmin
date: 23.09.30
title: 모음 사전
time: 30분
"""
order = 0    
dic = {}
lst =["A","E","I","O","U"] 

def solution(word):
    answer = 0
    dfs("")
    return dic[word]

def dfs(s):
    global order, dic, lst
    if len(s) > 5:
        return
    dic[s] = order
    order += 1
    for i in lst:
        if(len(s+i) > 5):
            return
        dfs(s + i)
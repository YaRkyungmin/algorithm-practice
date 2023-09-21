"""
author: kyungmin
date: 23.09.21
title: 단어 변환
time: 30분
"""

word_len = 0
answer = 0
def solution(begin, target, words):
    global word_len, answer
    word_len = len(begin)
    
    dfs(begin, target, words, 0)
    
    return answer

def dfs(word, target, words, depth):
    global answer
    
    # 글자가 같으면 return
    if word == target:
        answer = depth
        return
    
    word_list = words[:]
    dfs_list = []
    
    # 글자가 하나만 다른 word 찾아서 dfs_list 추가
    for i in word_list:
        count = 0
        for x in range(word_len):
            if word[x] == i[x]:
                count += 1
        
        if count == (word_len - 1):
            dfs_list.append(i)
    
    # 남은 word_list
    for i in dfs_list:
        word_list.remove(i)
    
    # dfs 재귀
    while dfs_list:
        pop_word = dfs_list.pop()
        dfs(pop_word, target, word_list, depth + 1)
    
    return
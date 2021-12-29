# autor: YaRkyungmin
# 2021-12-29
# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    new_id = new_id.lower() # step1
    for word in new_id: #step2
        if word.isalnum() or word in '-_.':
            answer += word
    while '..' in answer: #step3
        answer = answer.replace('..','.')
    answer = answer[1:] if answer[0]=='.' and len(answer) > 1 else answer #step4
    answer = answer[:-1] if answer[-1]=='.' else answer
    answer = 'a' if answer==str() else answer #step5
    if len(answer) > 15: #step6
        answer = answer[:15]
        answer = answer[:-1] if answer[-1]=='.' else answer
    while len(answer) < 3: #step7
        answer= answer+answer[-1]
    return answer

# 정규식으로 푼 다른풀이
# from re import sub

# def solution(new_id):
#     new_id = new_id.lower()
#     new_id = sub("[^a-z0-9-_.]", "", new_id)
#     new_id = sub("\.+", ".", new_id)
#     new_id = sub("(^\.|\.$)", "", new_id)
#     new_id = new_id if new_id else "a"
#     new_id = sub("\.$", "", new_id[:15])
#     new_id = new_id if len(new_id) > 3 else new_id + new_id[-1] * (3 - len(new_id))
#     return new_id
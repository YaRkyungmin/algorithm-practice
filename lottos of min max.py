# autor: YaRkyungmin
# 2021-12-28
# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3#fnref1
# programmers_로또의 최고 순위와 최저 순위_level-1

def solution(lottos, win_nums):
    answer = []
    dic_win = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    correct_count = 0
    zero_count = 0
    for i in range(6):
        if lottos[i] in win_nums:
            correct_count += 1
        elif lottos[i] == 0:
            zero_count += 1
    max_count = correct_count+zero_count
    answer = [dic_win[max_count],dic_win[correct_count]]
    return answer
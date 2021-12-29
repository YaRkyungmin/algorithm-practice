# autor: YaRkyungmin
# 2021-12-29
# https://programmers.co.kr/learn/courses/30/lessons/81301
# programmers_숫자 문자열과 영단어_level-1

'''
*enumerate
for문에서 index변수 없이 실행가능하게 해줌

*isdigit()
str이 숫자인지를 판단하여 bool값을 반환

*isalpha()
str이 알파벳인지를 판단하여 bool값을 반환

*dictionary key
dict_name.keys()
value값을 반환해준다
'''

def solution(s):
    num_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = ''
    for idx, num in enumerate(num_list):
        if num in s:
            s = s.replace(num,str(idx))
        answer = s
    answer = int(answer)
    return answer

## isdigit, isalpha를 이용한 다른 풀이
# def solution(s):
#     num_dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
#     answer = ''
#     english = ''
#     for i in s:
#         if i.isdigit():
#             answer += i
#         elif i.isalpha():
#             english += i
#             if english in num_dic.keys():
#                 answer += str(num_dic[english])
#                 english = ''
#     answer = int(answer)
#     return answer
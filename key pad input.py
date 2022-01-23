# autor: YaRkyungmin
# 2021-12-31
# https://programmers.co.kr/learn/courses/30/lessons/67256
# programmers_키패드 누르기_level-1

def solution(numbers, hand):
    keypad = {
    1 : (0,3), 2 : (1,3), 3 : (2,3),
    4 : (0,2), 5 : (1,2), 6 : (2,2),
    7 : (0,1), 8 : (1,1), 9 : (2,1),
    0 : (1,0)}
    answer = ''
    left_finger = [1,4,7]
    right_finger = [3,6,9]
    start_left_finger = (0,0)
    start_right_finger = (2,0)
    
    for button in numbers:
        if button in left_finger:
            answer += 'L'
            start_left_finger = keypad[button]
        elif button in right_finger:
            answer += 'R'
            start_right_finger = keypad[button]
        else:
            if abs(start_right_finger[0] - keypad[button][0]) + abs(start_right_finger[1] - keypad[button][1]) == abs(start_left_finger[0] - keypad[button][0]) + abs(start_left_finger[1] - keypad[button][1]):
                if hand == 'left':
                    answer += 'L'
                    start_left_finger = keypad[button]
                else:
                    answer += 'R'
                    start_right_finger = keypad[button]
            elif abs(start_right_finger[0] - keypad[button][0]) + abs(start_right_finger[1] - keypad[button][1]) < abs(start_left_finger[0] - keypad[button][0]) + abs(start_left_finger[1] - keypad[button][1]):
                answer += 'R'
                start_right_finger = keypad[button]
            else:
                answer += 'L'
                start_left_finger = keypad[button]

    return answer

# 유클리드 거리 = root((x2-x1)^2 + (y2 - y1)^2)
# 멘하탄 거리 = |x1 - x2| + |y1 - y2|

"""
author: kyungmin
date: 24.1.31
title: 1로 만들기 2
time: 30분
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [[0, []] for _ in range(N + 1)]

def find_min_idx(dist):
    idx = 0
    m_value = dist[0]
    for i in range(1, len(dist)):
        if dist[i] < m_value:
            idx = i
            m_value = dist[i]

    return idx, m_value

def mkr(idx, i):
    if idx == 0:
        return i // 3
    elif idx == 1:
        return i // 2
    else:
        return i - 1
    
def mkr1(idx, i):
    if idx == 0:
        return i // 3
    else:
        return i - 1

def mkr2(idx, i):
    if idx == 0:
        return i // 2
    else:
        return i - 1

dp[1][1] = [1]

if N >= 2:
    dp[2][0] = 1
    dp[2][1] = [1, 2]
if N >= 3:
    dp[3][0] = 1
    dp[3][1] = [1, 3]

if N > 3:
    for i in range(4, N + 1):
        if i % 3 == 0 and i % 2 == 0:
            li = [dp[i // 3][0], dp[i // 2][0], dp[i - 1][0]]
            idx, m_value = find_min_idx(li)
            dp[i][0] = m_value + 1
            ali = list(dp[mkr(idx, i)][1])
            ali.append(i)
            dp[i][1] = ali
        elif i % 3 == 0:
            li = [dp[i // 3][0], dp[i - 1][0]]
            idx, m_value = find_min_idx(li)
            dp[i][0] = m_value + 1
            ali = list(dp[mkr1(idx, i)][1])
            ali.append(i)
            dp[i][1] = ali
        elif i % 2 == 0:
            li = [dp[i // 2][0], dp[i - 1][0]]
            idx, m_value = find_min_idx(li)
            dp[i][0] = m_value + 1
            ali = list(dp[mkr2(idx, i)][1])
            ali.append(i)
            dp[i][1] = ali
        else:
            dp[i][0] = dp[i - 1][0] + 1
            ali = list(dp[i - 1][1])
            ali.append(i)
            dp[i][1] = ali
    

print(dp[N][0])
print(*sorted(dp[N][1], reverse = True))
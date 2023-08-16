"""
author: kyungmin
date: 23.08.15
title: 집합의 표현
time: 30분
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

array = [i for i in range(n+1)]

def find_parent(node):
    input_node = node
    while node != array[node]:
        node = array[node]
    array[input_node] = node
    return node

result = []
for _ in range(m):
    c, a, b = map(int, input().rstrip().split())
    if c == 0:
        a_parent = find_parent(a)
        b_parent = find_parent(b)
        if a_parent < b_parent:
            array[b_parent] = a_parent
        else:
            array[a_parent] = b_parent
    else:
        if find_parent(a) == find_parent(b):
            result.append("YES")
        else:
            result.append("NO")

print(*result, sep="\n")
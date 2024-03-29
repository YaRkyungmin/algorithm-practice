"""
author: kyungmin
date: 23.07.18
title: 버블 소트
time: 30분
"""
import sys
input = sys.stdin.readline
# print = sys.stdout.write

def merge(left, right):
    global cnt
    # left, right = len(left), len(right)
    i, j = 0, 0
    temp = []
    while i < len(left) and j < len(right):

        if left[i] > right[j]:
            temp.append(right[j])
            j += 1
            cnt += len(left) - i  # 왼쪽과 오른쪽을 비교했을 때 만약 오른쪽이 왼쪽보다 작다면,
            # 왼쪽의 남은 확인하지않은 인덱스들은 오른쪽보다는 당연히 큰 값으로 남아있으므로
            # 그 수만큼 갯수를 더해주면 됩니다.

        else:
            temp.append(left[i])
            i += 1

    if i == len(left):
        temp.extend(right[j:])
    else:
        temp.extend(left[i:])
    return temp


def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        mid = len(list) // 2
        left = merge_sort(list[: mid])
        right = merge_sort(list[mid:])
        return merge(left, right)


n = int(input())
cnt = 0
arr = list(map(int, input().split()))
arr = merge_sort(arr)
print(arr)
print(cnt)

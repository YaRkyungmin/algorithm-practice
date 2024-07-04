"""
author: kyungmin
date: 24.7.5
title: 가운데를 말해요
time: 30분
"""
# 백준에서 python3으로 채점했을때 시간초과 남. heap을 직접 구현해서 pypy로 채점을 해야함.
import sys
input = sys.stdin.readline

class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, x):
        self.data.append(x)
        idx = self.size() - 1
        while idx > 0:
            if self.data[idx] < self.data[(idx - 1) // 2]:
                self.swap(idx, (idx - 1) // 2)
                idx = (idx - 1) // 2
            else:
                break

    def chane_top(self, number):
        self.data[0] = number
        idx = 0
        size = self.size()
        while idx * 2 + 1 < size:
            left = idx * 2 + 1
            right = left + 1
            
            if right < size:
                c_idx = self.smaller(left, right)
                if self.data[idx] > self.data[c_idx]:
                    self.swap(c_idx, idx)
                    idx = c_idx
                else:
                    break

            elif left < size:
                if self.data[idx] > self.data[left]:
                    self.swap(left, idx)
                    idx = left
                else:
                    break
            else:
                break
    
    def size(self):
        return len(self.data)
    
    def smaller(self, a, b):
        if self.data[a] < self.data[b]:
            return a
        else:
            return b
        
    def swap(self, a, b):
        tmp = self.data[a]
        self.data[a] = self.data[b]
        self.data[b] = tmp
    
    def top(self):
        if self.size == 0:
            return IndexError
        else:
            return self.data[0]

minHeap = MinHeap()
maxHeap = MinHeap()

N = int(input().rstrip())

for _ in range(N):
    number = int(input().rstrip())
    if maxHeap.size() == minHeap.size():
        maxHeap.insert(-number)
    else:
        minHeap.insert(number)


    if minHeap.size() > 0 and -maxHeap.top() > minHeap.top():
        a = -maxHeap.top()
        maxHeap.chane_top(-minHeap.top())
        minHeap.chane_top(a)
    print(-maxHeap.top())

# class MaxHeap:
#     def __init__(self):
#         self.data = []

#     def insert(self, x):
#         self.data.append(x)
#         idx = self.size() - 1
#         while idx > 0:
#             if self.data[idx] > self.data[(idx - 1) // 2]:
#                 self.swap(idx, (idx - 1) // 2)
#                 idx = (idx - 1) // 2
#             else:
#                 break

#     def chane_top(self, number):
#         self.data[0] = number
#         idx = 0
#         size = self.size()
#         while idx * 2 + 1 < size:
#             left = idx * 2 + 1
#             right = left + 1
            
#             if right < size:
#                 c_idx = self.bigger(left, right)
#                 if self.data[idx] < self.data[c_idx]:
#                     self.swap(c_idx, idx)
#                     idx = c_idx
#                 else:
#                     break

#             elif left < size:
#                 if self.data[idx] < self.data[left]:
#                     self.swap(left, idx)
#                     idx = left
#                 else:
#                     break
#             else:
#                 break
    
#     def size(self):
#         return len(self.data)
    
#     def bigger(self, a, b):
#         if self.data[a] < self.data[b]:
#             return b
#         else:
#             return a
        
#     def swap(self, a, b):
#         tmp = self.data[a]
#         self.data[a] = self.data[b]
#         self.data[b] = tmp

#     def top(self):
#         if self.size == 0:
#             return IndexError
#         else:
#             return self.data[0]
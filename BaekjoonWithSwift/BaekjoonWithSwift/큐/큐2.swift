//
//  큐2.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 큐2() {
    let N = Int(readLine()!)!
    var head = 0
    var tail = 0
    var queue = Array(repeating: 0, count: N)
    
    for _ in 0..<N {
        let input = readLine()!.split(separator: " ").compactMap { String($0) }
        switch input.first {
        case "push":
            queue[tail % N] = Int(input.last!)!
            tail += 1
        case "pop":
            if head == tail {
                print(-1)
            } else {
                print(queue[head % N])
                head += 1
            }
        case "size":
            print(tail - head)
        case "empty":
            print(head == tail ? 1 : 0)
        case "front":
            print(head == tail ? -1 : queue[head % N])
        case "back":
            print(head == tail ? -1 : queue[(tail - 1) % N])
        default:
            continue
        }
    }
}

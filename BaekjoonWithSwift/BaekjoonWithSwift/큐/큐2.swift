//
//  큐2.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 큐2() {
    let N = Int(readLine()!)!
    var head: Node?
    var tail: Node?
    var size = 0
    var result = [String]()

    for _ in 0..<N {
        let input = readLine()!.split(separator: " ").compactMap { String($0) }

        switch input[0] {
        case "push":
            let node = Node(Int(input[1])!)
            
            if head == nil {
                head = node
                tail = node
                size += 1
            } else {
                tail?.next = node
                tail = node
                size += 1
            }
        case "pop":
            if head == nil {
                result.append("-1")
            } else if head?.next == nil {
                result.append(String(head!.value))
                head = nil
                tail = nil
                size -= 1
            } else {
                result.append(String(head!.value))
                head = head?.next
                size -= 1
            }
        case "size":
            result.append(String(size))
        case "empty":
            result.append(String(head == nil ? 1 : 0))
        case "front":
            result.append(String(head == nil ? -1 : head!.value))
        case "back":
            result.append(String(head == nil ? -1 : tail!.value))
        default:
            continue
        }
    }

    print(result.joined(separator: "\n"))

    class Node {
        var next: Node?
        let value: Int
        
        init(_ value: Int) {
            self.value = value
        }
    }
}

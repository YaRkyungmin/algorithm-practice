//
//  요세푸스문제.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 요세푸스문제() {
    let linkedList = LinkedList<Int>()

    let input = readLine()!.split(separator: " ").compactMap{ Int($0) }

    for i in 1...input[0] {
        linkedList.insert(i)
    }


    var result: [Int] = []

    for _ in 1...input[0] {
        result.append(linkedList.removeAt(input[1]))
    }

    print("<\(result.map { String($0) }.joined(separator: ", "))>")

    class LinkedList<T> {
        var head: Node<T>?
        var tail: Node<T>?

        func insert(_ value: T) {
            let node = Node(value: value)

            guard let headNode = head else {
                head = node
                tail = node
                return
            }

            guard let tailNode = tail else {
                return
            }

            tailNode.next = node
            tail = node
            node.next = headNode
        }

        func removeAt(_ point: Int) -> T {
            var removeNode = head
            
            for _ in 1..<point {
                removeNode = removeNode?.next
            }
            // 1 2 3 4 5 6 7
            head = removeNode?.next
            
            var tailNode = tail
            
            for _ in 1..<point {
                tailNode = tailNode?.next
            }
            
            tail = tailNode
            tail?.next = head
            
            return removeNode!.value
        }
    }

    class Node<T> {
        let value: T
        var next: Node<T>?

        init(value: T) {
            self.value = value
        }
    }
}

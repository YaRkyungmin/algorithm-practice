//
//  카드2.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 카드2() {
    let N = Int(readLine()!)!
    var head: Node?
    var tail: Node?
    var size = 0

    for i in 1...N {
        let node = Node(i)
        
        if head == nil {
            head = node
            tail = node
            size += 1
        } else {
            tail?.next = node
            tail = node
            size += 1
        }
    }

    while size > 1 {
        head = head?.next
        size -= 1
        
        if size == 1 {
            break
        }
        
        tail?.next = head
        head = head?.next
        tail = tail?.next
    }

    print(head!.value)

    class Node {
        var next: Node?
        let value: Int

        init(_ value: Int) {
            self.value = value
        }
    }
}

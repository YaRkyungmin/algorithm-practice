//
//  최솟값찾기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 최솟값찾기() {
    let NL = readLine()!.split(separator: " ").compactMap { Int($0)! }
    let numbers = readLine()!.split(separator: " ").compactMap { Int($0)! }
    var head: Node?
    var tail: Node?
    var result = [Int]()
    
    for (i, k) in numbers.enumerated() {
        let node = Node(k, i)
        
        guard let HNode = head else {
            head = node
            tail = node
            
            result.append(node.value)
            continue
        }
        
        var signal = false
        
        while node.value < tail!.value {
            tail = tail?.left
            tail?.right = nil
            
            if tail == nil {
                head = nil
                signal = true
                break
            }
        }
        
        if signal {
            head = node
            tail = node
            result.append(node.value)
            continue
            
        } else {
            tail?.right = node
            node.left = tail
            tail = node
        }
        
        if HNode.index == (i - NL[1]) {
            head = HNode.right
            head?.left = nil
        }
        
        result.append(head!.value)
    }
    
    print(result.map { String($0) }.joined(separator: " "))
    
    class Node {
        let value: Int
        let index: Int
        var left: Node?
        var right: Node?
        
        init(_ value: Int, _ index: Int) {
            self.value = value
            self.index = index
        }
    }
}

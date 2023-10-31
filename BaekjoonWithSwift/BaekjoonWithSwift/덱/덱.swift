//
//  덱.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 덱() {
    let N = Int(readLine()!)!
    var head: Node?
    var tail: Node?
    var size = 0
    
    for _ in 0..<N {
        let input = readLine()!.split(separator: " ").compactMap { String($0) }
        
        switch input.first! {
        case "push_front":
            size += 1
            let node = Node(Int(input.last!)!)
            
            guard let hNode = head else {
                head = node
                tail = node
                
                continue
            }
            
            hNode.left = node
            node.right = hNode
            head = node
            
        case "push_back":
            size += 1
            let node = Node(Int(input.last!)!)
            
            guard let tNode = tail else {
                head = node
                tail = node
                
                continue
            }
            
            tNode.right = node
            node.left = tNode
            tail = node
            
        case "pop_front":
            guard let hNode = head else {
                print(-1)
                continue
            }
            size -= 1
            print(hNode.value)
            
            guard let hRNode = hNode.right else {
                head = nil
                tail = nil
                continue
            }
            
            head = hRNode
            hRNode.left = nil
            
        case "pop_back":
            guard let tNode = tail else {
                print(-1)
                continue
            }
            size -= 1
            print(tNode.value)
            
            guard let tLNode = tNode.left else {
                head = nil
                tail = nil
                continue
            }
            
            tail = tLNode
            tLNode.right = nil

        case "size":
            print(size)
        case "empty":
            print(size == 0 ? 1 : 0)
        case "front":
            guard let hNode = head else {
                print(-1)
                continue
            }
            print(hNode.value)
        case "back":
            guard let tNode = tail else {
                print(-1)
                continue
            }
            print(tNode.value)
        default:
            continue
        }
    }
    
    class Node {
        let value: Int
        var left: Node?
        var right: Node?
        
        init(_ value: Int) {
            self.value = value
        }
    }
}

//
//  회전하는큐.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 회전하는큐() {
    let inputNM = readLine()!.split(separator: " ").compactMap { Int($0) }
    let numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    var head: Node?
    var tail: Node?
    var result = 0
    
    for i in 1...inputNM.first! {
        let node = Node(i)
        if head == nil {
            head = node
            tail = node
            continue
        }
        tail?.right = node
        node.left = tail
        tail = node
    }
    
    head?.left = tail
    tail?.right = head
    
    tail = nil
    
    for i in numbers {
        var move = 0
        var Rpoint = head
        var Lpoint = head
        var RSignal = false
        
        while Lpoint!.value != i && Rpoint!.value != i {
            move += 1
            
            Rpoint = Rpoint?.right
            Lpoint = Lpoint?.left
            
            if Rpoint?.value == i {
                RSignal = true
            }
        }
        
        result += move
        
        if RSignal {
            guard let RRpoint = Rpoint?.right else {
                head = nil
                continue
            }
            
            Rpoint?.left?.right = RRpoint
            RRpoint.left = Rpoint?.left
            
            head = RRpoint
        } else {
            guard let RLpoint = Lpoint?.right else {
                head = nil
                continue
            }
            
            Lpoint?.left?.right = RLpoint
            RLpoint.left = Lpoint?.left
            
            head = RLpoint
        }
    }
    
    print(result)
    
    class Node {
        let value: Int
        var left: Node?
        var right: Node?
        
        init(_ value: Int) {
            self.value = value
        }
    }
}

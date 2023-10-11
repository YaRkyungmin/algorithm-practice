//
//  에디터.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 에디터() {
    var inputString = readLine()!
    var commandArray: [[String]] = []

    let linkedList = LinkedList<String>()

    for i in inputString {
        linkedList.insertPoint(String(i))
    }

    for _ in 1...Int(readLine()!)! {
        let input = readLine()!.split(separator: " ").compactMap{ String($0) }
        
        switch input[0] {
        case "L":
            linkedList.leftMove()
        case "D":
            linkedList.dleftMove()
        case "B":
            linkedList.removePoint()
        case "P":
            linkedList.insertPoint(input[1])
        default :
            continue
        }
    }

    while let firstString = linkedList.removeFirst() {
        print(firstString, terminator: "")
    }

    final class LinkedList<T> {
        var head: Node<T>?
        var point: Node<T>?
        
        func removeFirst() -> T? {
            guard let head = head else {
                return nil
            }
            
            guard let backNode = head.back else {
                self.head = nil
                return head.value
            }
            
            self.head = backNode
            self.head?.previous = nil
            
            return head.value
        }
        
        func leftMove() {
            guard let previousNode = point?.previous else {
                point = nil
                return
            }

            point = previousNode
        }
        
        func dleftMove() {
            guard let head = head else {
                return
            }
            guard let point = point else {
                self.point = head
                return
            }
            
            guard let backNode = point.back else {
                return
            }

            self.point = backNode
        }
        
        func insertPoint(_ value: T) {
            let node = Node(value)
            
            guard let head = self.head else {
                self.head = node
                self.point = node
                
                return
            }
            
            guard let point = self.point else {
                head.previous = node
                node.back = head
                self.point = node
                self.head = node
                
                return
            }
            
            guard let backNode = point.back else {
                point.back = node
                node.previous = point
                self.point = node
                
                return
            }
            
            backNode.previous = node
            node.back = backNode
            node.previous = point
            point.back = node
            self.point = node
        }


        func removePoint() {
            guard let point = self.point else {
                return
            }
            
            guard let previousNode = point.previous else {
                self.head = point.back
                self.head?.previous = nil
                self.point = nil
                
                return
            }
            
            guard let backNode = point.back else {
                self.point = previousNode
                previousNode.back = nil
                
                return
            }
            
            previousNode.back = backNode
            backNode.previous = previousNode
            
            self.point = previousNode
            
            return
        }
    }

    final class Node<T> {
        var back: Node<T>?
        var previous: Node<T>?
        var value: T
        
        init(_ value: T) {
            self.value = value
        }
    }
}

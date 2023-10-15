//
//  스택.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 스택() {
    let N = Int(readLine()!)!
    var stack: [String] = []

    for _ in 0..<N {
        let order = readLine()!.split(separator: " ").compactMap { String($0) }
        
        switch order[0] {
        case "push":
            stack.append(order[1])
        case "top":
            if stack.isEmpty == false {
                print(stack.last!)
            } else {
                print("-1")
            }
        case "size":
            print(stack.count)
        case "empty":
            if stack.isEmpty {
                print("1")
            } else {
                print("0")
            }
        case "pop":
            if stack.isEmpty == false {
                print(stack.removeLast())
            } else {
                print("-1")
            }
        default:
            print("", terminator: "")
        }
    }
}

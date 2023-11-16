//
//  좋은단어.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/27.
//

import Foundation

func 좋은단어() {
    let N = Int(readLine()!)!
    var count = 0
    
    for _ in 0..<N {
        var stack = [String]()
        let input = readLine()!.compactMap { String($0) }
        for i in (0..<input.count).reversed() {
            switch input[i] {
            case "A":
                if stack.count > 0 {
                    if stack.last! == "A" {
                        stack.removeLast()
                    } else {
                        stack.append("A")
                    }
                } else {
                    stack.append("A")
                }
            case "B":
                if stack.count > 0 {
                    if stack.last! == "B" {
                        stack.removeLast()
                    } else {
                        stack.append("B")
                    }
                } else {
                    stack.append("B")
                }
            default:
                continue
            }
        }
        
        if stack.count == 0 {
            count += 1
        }
    }
    print(count)
}

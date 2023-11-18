//
//  괄호.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/27.
//

import Foundation

func 괄호() {
    let N = Int(readLine()!)!
    
    for _ in 0..<N {
        var signal = true
        var stack = [String]()
        let input = readLine()!.compactMap { String($0) }
        for i in (0..<input.count).reversed() {
            switch input[i] {
            case "(":
                if stack.count > 0 {
                    stack.removeLast()
                } else {
                    signal = false
                    break
                }
            case ")":
                stack.append(")")
            default:
                continue
            }
        }
        
        if stack.count > 0 {
            signal = false
        }
        print(signal ? "YES" : "NO")
    }
}

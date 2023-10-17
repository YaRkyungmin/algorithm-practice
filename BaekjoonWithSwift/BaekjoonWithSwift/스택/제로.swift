//
//  제로.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 제로() {
    let N = Int(readLine()!)!
    var stack: [Int] = []

    for _ in 0..<N {
        let input = Int(readLine()!)!
        
        if input == 0 {
            stack.removeLast()
        } else {
            stack.append(input)
        }
    }

    print(stack.reduce(0) { $0 + $1 })
}

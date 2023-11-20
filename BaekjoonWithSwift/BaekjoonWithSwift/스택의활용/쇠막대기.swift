//
//  쇠막대기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/27.
//

import Foundation

func 쇠막대기() {
    var count = 0
    var stack = 0
    let input = readLine()!.compactMap { String($0) }
    var signal = false
    var pre_count = 0
    for i in (0..<input.count).reversed() {
        switch input[i] {
        case "(":
            if signal {
                stack -= 1
                count += stack - pre_count
                pre_count = 0
                signal = false
            } else {
                count += stack - pre_count
                stack -= 1
                pre_count = stack
            }
        case ")":
            stack += 1
            signal = true
        default:
            continue
        }
    }
    print(count)
}

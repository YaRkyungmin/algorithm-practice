//
//  스택수열.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 스택수열() {
    let N = Int(readLine()!)!
    var number = 0
    var stack: [Int] = []
    var output = ""

    for _ in 0..<N {
        let input = Int(readLine()!)!
        
        while number < input {
            number += 1
            stack.append(number)
            output += "+"
        }
        
        if input == stack.removeLast() {
            output += "-"
        } else {
            output = "NO"
            break
        }
    }

    if output == "NO" {
        print(output)
    } else {
        output.forEach { print($0) }
    }
}

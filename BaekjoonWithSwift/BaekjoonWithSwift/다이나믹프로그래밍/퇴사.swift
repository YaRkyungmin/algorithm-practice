//
//  퇴사.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/22.
//

import Foundation

func 퇴사() {
    let N = Int(readLine()!)!
    var consult = [(Int, Int)]()
    for _ in 0..<N {
        let input = readLine()!.split(separator: " ").compactMap { Int($0) }
        consult.append((input[0], input[1]))
    }
    var dp = Array(repeating: 0, count: N)
    for i in (0..<N).reversed() {
        let (d, w) = consult[i]
        
        if i + d - 1 >= N {
            continue
        }
        
        var sum = 0
        
        for x in i...(i + d - 1) {
            sum += dp[x]
        }
        
        if sum < w {
            dp[i] = w - sum
        }
    }
    var result = 0
    
    for i in 0..<N {
        result += dp[i]
    }
    print(result)
}


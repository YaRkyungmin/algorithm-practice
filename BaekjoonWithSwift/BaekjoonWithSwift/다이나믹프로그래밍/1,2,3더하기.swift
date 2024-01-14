//
//  1,2,3더하기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/14.
//

import Foundation

func 일이삼더하기() {
    let T = Int(readLine()!)!
    var dp = Array(repeating: 0, count: 12)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    var m = 1
    var input = [Int]()
    
    for _ in 0..<T {
        let n = Int(readLine()!)!
        input.append(n)
        m = max(m, n)
    }
    
    if m > 3 {
        for i in 4...m {
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        }
    }
    
    for x in input {
        print(dp[x])
    }
}

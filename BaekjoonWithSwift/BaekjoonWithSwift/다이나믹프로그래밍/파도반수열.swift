//
//  파도반수열.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/22.
//

import Foundation

func 파도반수열() {
    let T = Int(readLine()!)!
    var dp = [1, 1, 1, 2, 2] + Array(repeating: 0, count: 95)
    var m = 0
    var reA = Array(repeating: 0, count: T)
    for i in 0..<T {
        let N = Int(readLine()!)!
        reA[i] = N
        m = max(N, m)
    }
    if m > 5 {
        for i in 5..<m {
            dp[i] = dp[i - 1] + dp[i - 5]
        }
    }
    var result = ""
    for i in reA {
        result += String(dp[i - 1]) + "\n"
    }
    print(result)
}

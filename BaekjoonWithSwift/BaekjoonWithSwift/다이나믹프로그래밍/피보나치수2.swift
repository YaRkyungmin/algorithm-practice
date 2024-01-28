//
//  피보나치수2.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/28.
//

import Foundation

func 피보나치수2() {
    let n = Int(readLine()!)!
    
    var dp = Array(repeating: 0, count: n + 1)
    dp[1] = 1
    
    if n > 1 {
        for i in 2...n {
            dp[i] = dp[i - 1] + dp[i - 2]
        }
    }

    print(dp[n])
}

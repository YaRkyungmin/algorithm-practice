//
//  쉬운계단수.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/16.
//

import Foundation

func 쉬운계단수() {
    let N = Int(readLine()!)!
    var dp = Array(repeating: 0, count: N)
    dp[0] = 9
    for i in 1..<N {
        dp[i] = (dp[i - 1] * 2 - i) % 1000000000
    }
    
    print(dp[N - 1])
}

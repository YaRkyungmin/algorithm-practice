//
//  2xn타일링2.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/18.
//

import Foundation

func 이n타일링투() {
    let n = Int(readLine()!)!
    
    var dp = Array(repeating: 0, count: n)
    dp[0] = 1
    var signal = 1
    
    for i in 1..<n {
        dp[i] = (dp[i-1]*2 + signal) % 10007
        signal = signal == 1 ? -1 : 1
    }
    print(dp[n-1])
}

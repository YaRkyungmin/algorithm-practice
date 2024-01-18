//
//  2xn타일링.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/18.
//

import Foundation

func 이n타일링() {
    let n = Int(readLine()!)!
    
    var dp = Array(repeating: 0, count: n)
    dp[0] = 1
    if n >= 2 {
        dp[1] = 2
        
        for i in 2..<n {
            dp[i] = (dp[i-2] + dp[i-1]) % 10007
        }
    }
    print(dp[n-1])
}

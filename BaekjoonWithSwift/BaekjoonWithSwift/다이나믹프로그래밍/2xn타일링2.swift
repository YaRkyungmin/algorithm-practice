//
//  2xn타일링2.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/18.
//

import Foundation

func 이n타일링투() {
    let n = Int(readLine()!)!
    
    var dp = Array(repeating: 1, count: n + 1)

    if n >= 2 {
        for i in 2...n {
            dp[i] = (dp[i-1] + (2 * dp[i-2])) % 10007
        }
    }
    print(dp[n])
}

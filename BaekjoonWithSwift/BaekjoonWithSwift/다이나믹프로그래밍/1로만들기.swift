//
//  1로만들기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/13.
//

import Foundation

func 일로만들기() {
    let N = Int(readLine()!)!
    var dp = Array(repeating: 100000, count: N + 1)
    
    dp[1] = 0
    
    if N > 1 {
        findMin(m: 2)
    }
    // bottom up
    func findMin(m: Int) {
        if m % 2 == 0 && m % 3 == 0 {
            dp[m] = min(dp[m/3] + 1 , dp[m/2] + 1, dp[m-1] + 1)
        } else if m % 2 == 0 {
            dp[m] = min(dp[m/2] + 1, dp[m-1] + 1)
        } else if m % 3 == 0 {
            dp[m] = min(dp[m/3] + 1, dp[m-1] + 1)
        } else {
            dp[m] = dp[m-1] + 1
        }
        
        if m == N {
            return
        }
        
        findMin(m: m + 1)
    }
    
    print(dp[N])
}

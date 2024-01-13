//
//  1로만들기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/13.
//

import Foundation

func 일로만들기() {
    let N = Int(readLine()!)!
    var dp = [Int: Int]()
    dp[1] = 0
    // top_down
    func findMin(m: Int) -> Int {
        if dp.keys.contains(m) {
            return dp[m]!
        }
        
        if m % 3 == 0 && m % 2 == 0 {
            dp[m] = min(findMin(m: m / 3) + 1, findMin(m: m / 2) + 1)
        } else if m % 3 == 0 {
            dp[m] = min(findMin(m: m / 3) + 1, findMin(m: m - 1) + 1)
        } else if m % 2 == 0 {
            dp[m] = min(findMin(m: m / 2) + 1, findMin(m: m - 1) + 1)
        } else {
            dp[m] = findMin(m: m - 1) + 1
        }
        
        return dp[m]!
    }
    
    print(findMin(m: N))
}

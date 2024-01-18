//
//  이친수.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/18.
//

import Foundation

func 이친수() {
    let N = Int(readLine()!)!
    
    var dp = Array(repeating: 0, count: N)
    dp[0] = 1
    var numbers = (0, 1)
    
    for i in 1..<N {
        var newNum = (0, 0)
        
        newNum.0 += numbers.0
        newNum.1 += numbers.0
        newNum.0 += numbers.1
        dp[i] = newNum.0 + newNum.1
        numbers = newNum
    }
    
    print(dp[N-1])
}

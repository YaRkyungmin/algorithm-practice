//
//  가장긴증가하는부분수열.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/21.
//

import Foundation

func 가장긴증가하는부분수열() {
    let N = Int(readLine()!)!
    let numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    var dp = Array(repeating: 0, count: N)
    dp[0] = 1
    var result = dp[0]
    
    for i in 1..<N {
        let fix = numbers[i]
        var sum = 0
        for x in (0..<i).reversed() {
            if fix > numbers[x] {
                sum = max(dp[x], sum)
            }
        }
        dp[i] = sum + 1
        result = max(dp[i], result)
    }
    
    print(result)
}

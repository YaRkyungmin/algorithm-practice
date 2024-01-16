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
    var num = Array(repeating: 1, count: 11)
    num[0] = 0
    dp[0] = 9
    let rule = [(1, 10), (0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10)]
    for i in 1..<N {
        var copy = Array(repeating: 0, count: 11)
        for x in 0..<10 {
            copy[rule[x].0] += (num[x] % 1000000000)
            copy[rule[x].1] += (num[x] % 1000000000)
        }
        var sum = 0
        for x in 0..<10 {
            sum += copy[x]
        }
        dp[i] = (sum % 1000000000)
        num = copy
    }
    print(dp[N - 1])
}

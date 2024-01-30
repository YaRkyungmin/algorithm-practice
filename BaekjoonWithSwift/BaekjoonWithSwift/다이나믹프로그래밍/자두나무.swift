//
//  자두나무.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/29.
//

import Foundation

func 자두나무() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let T = input[0]
    let W = input[1]
    
    var tree = Array(repeating: 0, count: T)
    for i in 0..<T {
        tree[i] = Int(readLine()!)!
    }
    
    var dp = Array(repeating: Array(repeating: 0, count: T), count: W + 2)
    var result = 1
    
    for x in 0..<T {
        for y in 0...W {
            if x == 0 {
                if tree[x] == 1 {
                    dp[y][x] = y % 2 == 0 ? 1 : 0
                } else {
                    dp[y][x] = y % 2 == 0 ? 0 : 1
                }
            } else {
                dp[y][x] = max(dp[y][x - 1], dp[y + 1][x - 1])
                
                if tree[x] == 1 {
                    dp[y][x] += y % 2 == 0 ? 1 : 0
                } else {
                    dp[y][x] += y % 2 == 0 ? 0 : 1
                }
                
                result = max(dp[y][x], result)
            }
        }
    }
    
    print(result)
}

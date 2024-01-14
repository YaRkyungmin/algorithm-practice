//
//  계단오르기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/15.
//

import Foundation

func 계단오르기() {
    let N = Int(readLine()!)!
    var numbers = [Int]()
    
    for _ in 0..<N {
        let n = Int(readLine()!)!
        numbers.append(n)
    }
    // top-down
    if numbers.count == 2 {
        print(numbers[0] + numbers[1])
    } else if numbers.count == 3 {
        print(max(numbers[0] + numbers[2], numbers[1] + numbers[2]))
    } else if numbers.count == 1 {
        print(numbers[0])
    } else {
        var dp = Array(repeating: (0, 0), count: numbers.count)
        let one = numbers[N - 1]
        let two = numbers[N - 2]
        let three = numbers[N - 3]
        dp[N - 1] = (one, one)
        dp[N - 2] = (one + two, one + two)
        dp[N - 3] = (one + three, one + three)
        
        for i in (0...(N - 4)).reversed() {
            dp[i] = (dp[i + 1].1 + numbers[i], max(dp[i + 2].0, dp[i + 2].1) + numbers[i])
        }
        
        print(max(dp[0].0, dp[0].1, dp[1].0, dp[1].1))
    }
}


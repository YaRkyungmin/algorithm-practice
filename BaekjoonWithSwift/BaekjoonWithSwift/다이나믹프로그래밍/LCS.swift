//
//  LCS.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/25.
//

import Foundation

func LCS() {
    let str1 = readLine()!.map { String($0) }
    let str2 = readLine()!.map { String($0) }
    var dp = Array(repeating: 0, count: str1.count)
    var result = 0
    
    for i in 0..<str2.count {
        if str1[0] == str2[i] {
            dp[0] = i
            result = 1
            break
        }
    }
    
    if str1.count > 1 {
        for i in 1..<str1.count {
            for z in (0...i).reversed(){
                for x in dp[z]..<str2.count {
                    if x == dp[z] {
                        continue
                    }
                    
                    if str1[i] == str2[x] {
                        dp[i] = max(dp[i], x)
                        break
                    }
                }
            }
        }
        
        var newDp = Array(repeating: 0, count: str1.count)
        
        for i in 0..<str1.count {
            for x in (0..<i).reversed() {
                if dp[i] > dp[x] {
                    newDp[i] = max(newDp[x], newDp[i])
                }
            }
            newDp[i] += 1
            result = max(newDp[i], result)
        }
    }
    print(result)
}

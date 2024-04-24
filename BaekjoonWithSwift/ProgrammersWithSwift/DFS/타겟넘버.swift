//
//  타겟넘버.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/04/24.
//

import Foundation

func 타겟넘버() {
    func solution(_ numbers:[Int], _ target:Int) -> Int {
        var result = 0
        func dfs(_ depth: Int, _ sum: Int) {
            if depth == numbers.count {
                if sum == target {
                    result += 1
                }
                return
            }
            dfs(depth + 1, sum + numbers[depth])
            dfs(depth + 1, sum - numbers[depth])
        }
        
        dfs(0, 0)
        
        return result
    }
}

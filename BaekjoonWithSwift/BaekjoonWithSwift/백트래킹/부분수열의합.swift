//
//  부분수열의합.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/24.
//

import Foundation

func 부분수열의합() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let S = input[1]
    
    let permutation = readLine()!.split(separator: " ").compactMap { Int($0) }
    var cnt = 0
    
    func findS(sum: Int, k: Int) {
        for i in k..<N {
            let newSum = permutation[i] + sum
            cnt += (newSum == S) ? 1 : 0
            findS(sum: newSum, k: i + 1)
        }
    }
    
    findS(sum: 0, k: 0)
    print(cnt)
}

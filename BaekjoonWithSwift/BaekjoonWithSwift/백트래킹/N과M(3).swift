//
//  N과M(3).swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/26.
//

import Foundation

func N과M3() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    let permutation = Array(1...N)
    var pArr = Array(repeating: 0, count: M)
    var result = [String]()
    
    func findPermutation(k: Int) {
        if k == M {
            result.append(pArr.map { String($0) }.joined(separator: " "))
            return
        }

        for i in 0..<N {
            pArr[k] = permutation[i]
            findPermutation(k: k + 1)
        }
    }
    
    findPermutation(k: 0)
    print(result.joined(separator: "\n"))
}

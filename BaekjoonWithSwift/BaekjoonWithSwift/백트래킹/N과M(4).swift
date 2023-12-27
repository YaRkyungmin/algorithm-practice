//
//  N과M(4).swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/27.
//

import Foundation

func N과M4() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    let numbers = Array(1...N)
    var arr = Array(repeating: 0, count: M)
    var result = ""
    
    func permutation(k: Int, max: Int) {
        if k == M {
            result += arr.map { String($0) }.joined(separator: " ") + "\n"
            return
        }
        
        for i in max..<N {
            arr[k] = numbers[i]
            permutation(k: k + 1, max: i)
        }
    }
    permutation(k: 0, max: 0)
    print(result)
}

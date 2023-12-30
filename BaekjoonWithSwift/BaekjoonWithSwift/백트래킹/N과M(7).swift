//
//  N과M(7).swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/30.
//

import Foundation

func N과M7() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    var numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    numbers.sort()
    var arr = Array(repeating: 0, count: M)
    var result = ""
    
    func permutation(k: Int) {
        if k == M {
            result += arr.map { String($0) }.joined(separator: " ") + "\n"
            return
        }
        
        for i in 0..<N {
            arr[k] = numbers[i]
            permutation(k: k + 1)
        }
    }
    
    permutation(k: 0)
    print(result)
}

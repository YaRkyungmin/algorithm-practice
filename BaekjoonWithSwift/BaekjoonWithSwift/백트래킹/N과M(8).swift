//
//  N과M(8).swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/31.
//

import Foundation

func N과M8() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    var numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    numbers.sort()
    var result = ""
    
    func permutation(k: Int, max: Int, pStr: String) {
        if k == M {
            result += pStr + "\n"
            return
        }
        
        for i in max..<N {
            permutation(k: k + 1, max: i, pStr: pStr + String(numbers[i]) + " ")
        }
    }
    
    permutation(k: 0, max: 0, pStr: "")
    print(result)
}

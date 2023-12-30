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
    var result = ""
    
    func permutation(k: Int, pStr: String) {
        if k == M {
            result += pStr + "\n"
            return
        }
        
        for i in 0..<N {
            permutation(k: k + 1, pStr: pStr + String(numbers[i]) + " ")
        }
    }
    
    permutation(k: 0, pStr: "")
    print(result)
}

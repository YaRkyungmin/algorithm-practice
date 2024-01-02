//
//  N과M(11).swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/02.
//

import Foundation

func N과M11() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    var numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    numbers.sort()
    var result = ""
    var strSet = Set<String>()
    
    func permutation(k: Int, pStr: String) {
        if k == M {
            if strSet.contains(pStr) {
                return
            } else {
                result += pStr + "\n"
                strSet.insert(pStr)
                return
            }
        }
        
        for i in 0..<N {
            permutation(k: k + 1, pStr: pStr + String(numbers[i]) + " ")
        }
    }
    
    permutation(k: 0, pStr: "")
    print(result)
}

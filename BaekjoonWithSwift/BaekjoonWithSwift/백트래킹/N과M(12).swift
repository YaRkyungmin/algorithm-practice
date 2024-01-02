//
//  N과M(12).swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/02.
//

import Foundation

func N과M12() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    var numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    numbers.sort()
    var result = ""
    var strSet = Set<String>()
    
    func permutation(k: Int, max: Int, pStr: String) {
        if k == M {
            if strSet.contains(pStr) {
                return
            } else {
                result += pStr + "\n"
                strSet.insert(pStr)
                return
            }
        }
        
        for i in max..<N {
            permutation(k: k + 1, max: i, pStr: pStr + String(numbers[i]) + " ")
            
        }
    }
    
    permutation(k: 0, max: 0, pStr: "")
    print(result)
}

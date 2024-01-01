//
//  N과M(9).swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/01.
//

import Foundation

func N과M9() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    var numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    numbers.sort()
    var result = ""
    var strSet = Set<String>()
    var visit = Array(repeating: false, count: N)
    
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
            if !visit[i] {
                visit[i] = true
                permutation(k: k + 1, pStr: pStr + String(numbers[i]) + " ")
                visit[i] = false
            }
        }
    }
    
    permutation(k: 0, pStr: "")
    print(result)
}

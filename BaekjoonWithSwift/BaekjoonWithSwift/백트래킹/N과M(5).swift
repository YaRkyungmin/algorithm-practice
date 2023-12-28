//
//  N과M(5).swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/28.
//

import Foundation

func N과M5() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    var numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    numbers.sort()
    var arr = Array(repeating: 0, count: M)
    var result = ""
    var visit = Array(repeating: false, count: N)
    
    func permutation(k: Int) {
        if k == M {
            result += arr.map { String($0) }.joined(separator: " ") + "\n"
            return
        }
        
        for i in 0..<N {
            if !visit[i] {
                arr[k] = numbers[i]
                visit[i] = true
                permutation(k: k + 1)
                visit[i] = false
            }
        }
    }
    
    permutation(k: 0)
    print(result)
}

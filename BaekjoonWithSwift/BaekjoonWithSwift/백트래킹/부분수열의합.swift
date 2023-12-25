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
    var set = Set<Int>()
    
    for i in 0..<N {
        set.insert(i)
    }
    
    var cnt = 0
    
    func findS(arr: Set<Int>, sum: Int) {
        if arr.count == 0 {
            return
        }
        
        for i in arr {
            let newSum = permutation[i] + sum
            cnt += (newSum == S) ? 1 : 0
            var newArr = arr
            newArr.remove(i)
            findS(arr: newArr, sum: newSum)
        }
    }
    
    findS(arr: set, sum: 0)
    print(cnt)
}


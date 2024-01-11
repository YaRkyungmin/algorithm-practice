//
//  빈도정렬.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/11.
//

import Foundation

func 빈도정렬() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let C = input[1]
    var numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    var numSet = Set<Int>()
    var onedic = [Int: Int]() // 빈도수
    var twodic = [Int: Int]() // 등장순서
    var sortNumbers = [(Int, Int, Int)]()
    
    for i in 0..<N {
        if !numSet.contains(numbers[i]) {
            numSet.insert(numbers[i])
            onedic[numbers[i]] = -1
            twodic[numbers[i]] = i
        } else {
            onedic[numbers[i]] =  onedic[numbers[i]]! - 1
        }
    }
    
    for i in numSet {
        sortNumbers.append((onedic[i]!, twodic[i]!, i))
    }
    
    sortNumbers.sort { ($0.0, $0.1) < ($1.0, $1.1) }
    
    var result = ""
    for (c, _, x) in sortNumbers {
        for _ in 0..<(-c) {
            result += String(x) + " "
        }
    }
    print(result)
}

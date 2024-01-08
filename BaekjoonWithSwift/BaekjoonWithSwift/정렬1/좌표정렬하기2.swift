//
//  좌표정렬하기2.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/09.
//

import Foundation

func 좌표정렬하기2() {
    let N = Int(readLine()!)!
    var numbers = [(Int, Int)]()
    for _ in 0..<N {
        let number = readLine()!.split(separator: " ").compactMap { Int($0) }
        numbers.append((number[0], number[1]))
    }
    
    numbers.sort { ($0.1, $0.0) < ($1.1, $1.0) }
    
    for (x, y) in numbers {
        print("\(x) \(y)")
    }
}

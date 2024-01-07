//
//  수정렬하기2.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/08.
//

import Foundation

func 수정렬하기2() {
    let N = Int(readLine()!)!
    var numbers = [Int]()
    for _ in 0..<N {
        numbers.append(Int(readLine()!)!)
    }
    numbers.sort()
    for i in numbers {
        print(i)
    }
}

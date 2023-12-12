//
//  곱셈.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/12.
//

import Foundation

func 곱셈() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let A = input[0]
    let B = input[1]
    let C = input[2]
    print(recursive(cnt: 0, total: 1))
    
    func recursive(cnt: Int, total: Int) -> Int {
        if cnt == B {
            return total % C
        }

        return recursive(cnt: cnt + 1, total: (total * A) % C )
    }
}

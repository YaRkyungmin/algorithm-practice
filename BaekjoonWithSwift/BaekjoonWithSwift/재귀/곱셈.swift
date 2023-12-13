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
    print(recursive(cnt: B))
    
    func recursive(cnt: Int) -> Int {
        if cnt == 0 {
            return 1
        }
        
        var tmp = recursive(cnt: cnt / 2) % C
        tmp = (tmp * tmp) % C
        
        if cnt % 2 == 0 {
            return tmp
        } else {
            return (tmp * A) % C
        }
    }
}

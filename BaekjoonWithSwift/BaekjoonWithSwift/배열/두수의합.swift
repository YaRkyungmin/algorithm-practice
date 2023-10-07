//
//  두수의합.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 두수의합() {
    let N = Int(String(readLine()!))!
    var array = readLine()!.split(separator: " ").map{Int(String($0))!}.sorted()
    let x = Int(String(readLine()!))!

    var setset = Set<Int>()

    for i in array {
        setset.insert(i)
    }

    var answer = 0

    for i in array {
        if setset.contains(x - i) {
            answer += 1
        }
    }
    print(answer/2)
}

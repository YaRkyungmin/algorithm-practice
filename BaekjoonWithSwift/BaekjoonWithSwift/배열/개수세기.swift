//
//  개수세기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 개수세기() {
    let N = Int(String(readLine()!))!
    var array = readLine()!.split(separator: " ").map{Int(String($0))!}.sorted()
    let x = Int(String(readLine()!))!

    var answer = 0
    for i in array {
        if i == x {
            answer += 1
        }
    }

    print(answer)
}

//
//  숫자의개수.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 숫자의개수() {
    let a = Int(readLine() ?? "0") ?? 0
    let b = Int(readLine() ?? "0") ?? 0
    let c = Int(readLine() ?? "0") ?? 0

    let sum = a * b * c

    let sumString = String(sum)
    var arrayRepeating = Array(repeating: 0, count: 10)

    for i in sumString {
        let convertInteger = Int(String(i)) ?? 0
        arrayRepeating[convertInteger] += 1
    }

    for i in arrayRepeating {
        print(i)
    }
}

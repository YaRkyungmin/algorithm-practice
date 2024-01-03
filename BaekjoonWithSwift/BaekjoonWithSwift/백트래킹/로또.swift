//
//  로또.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/03.
//

import Foundation

func 로또() {
    while true {
        let input = readLine()!.split(separator: " ").compactMap { Int($0) }
        if input[0] == 0 {
            break
        }
        let k = input[0]
        var numbers = [Int]()
        for i in 1...k {
            numbers.append(input[i])
        }
        
        var result = ""
        var visit = Array(repeating: false, count: numbers.count)
        
        func lotto(t: Int, max: Int, pStr: String) {
            if t == 6 {
                result += pStr + "\n"
                return
            }
            
            for i in max..<k {
                if !visit[i] {
                    visit[i] = true
                    lotto(t: t + 1, max: i + 1, pStr: pStr + String(numbers[i]) + " ")
                    visit[i] = false
                }
            }
        }
        lotto(t: 0, max: 0, pStr: "")
        print(result)
    }
}

//
//  같이눈사람만들래?.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/04/22.
//

import Foundation

func 같이눈사람만들래() {
    let N = Int(readLine()!)!
    var numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
    numbers.sort()
    var result = 1000000001
    var signal = false
    for i in stride(from: 0, to: N - 3, by: 1) {
        if signal { break }
        for j in stride(from: i + 3, to: N, by: 1) {
            let A = numbers[i] + numbers[j]
            var st = i + 1
            var en = j - 1
            while st < en {
                let B = numbers[st] + numbers[en]
                let diff = A - B
                if A > B {
                    result = min(result, abs(diff))
                    st += 1
                } else if A < B {
                    result = min(result, abs(diff))
                    en -= 1
                } else {
                    result = 0
                    signal = true
                    break
                }
            }
            if signal { break }
        }
    }
    print(result)
}

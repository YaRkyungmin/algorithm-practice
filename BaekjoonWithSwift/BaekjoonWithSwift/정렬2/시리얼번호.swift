//
//  시리얼번호.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/10.
//

import Foundation

func 시리얼번호() {
    let N = Int(readLine()!)!
    var serial = [(Int, Int, String)]()
    
    for _ in 0..<N {
        let st = readLine()!
        var sum = 0
        for i in st {
            let asciiNum = UnicodeScalar(String(i))!.value
            if asciiNum >= 49 && asciiNum <= 57 {
                sum += Int(String(i))!
            }
        }
        serial.append((st.count, sum, st))
    }
    
    serial.sort { ($0.0, $0.1, $0.2) < ($1.0, $1.1, $1.2) }
    
    for (_, _, s) in serial {
        print(s)
    }
}

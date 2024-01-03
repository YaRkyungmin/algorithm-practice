//
//  암호만들기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/04.
//

import Foundation

func 암호만들기() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let L = input[0]
    let C = input[1]
    var alphabet = readLine()!.split(separator: " ").compactMap { String($0) }
    alphabet.sort()
    var vowels: Set<String> = ["a", "e", "i", "o", "u"]
    var result = ""
    
    func findPassword(k: Int, max: Int, pStr: String, vCount: Int, cCount: Int) {
        if k == L {
            result += vCount > 0 && cCount > 1 ? pStr + "\n" : ""
            return
        }
        
        for i in max..<C {
            findPassword(
                k: k + 1,
                max: i + 1,
                pStr: pStr + alphabet[i],
                vCount: vCount + (vowels.contains(alphabet[i]) ? 1 : 0),
                cCount: cCount + (vowels.contains(alphabet[i]) ? 0 : 1)
            )
        }
    }
    
    findPassword(k: 0, max: 0, pStr: "", vCount: 0, cCount: 0)
    print(result)
}

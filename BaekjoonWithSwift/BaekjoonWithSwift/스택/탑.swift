//
//  탑.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 탑() {
    let N = Int(readLine()!)!

    let topArr = readLine()!.split(separator: " ").compactMap { Int($0) }
    var signalArr = Array(repeating: 0, count: N)
    var stack: [[Int]] = []

    for i in (0..<N).reversed() {
        if !stack.isEmpty {
            while topArr[i] >= stack.last![0] {
                let signalEle = stack.removeLast()
                signalArr[signalEle[1]] = i + 1
                
                if stack.isEmpty {
                    break
                }
            }
        }

        stack.append([topArr[i], i])
    }

    print(signalArr.map { String($0) }.joined(separator: " "))
}

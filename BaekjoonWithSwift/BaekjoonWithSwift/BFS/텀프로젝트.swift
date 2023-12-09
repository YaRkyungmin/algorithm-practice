//
//  텀프로젝트.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/09.
//

import Foundation

func 텀프로젝트() {
    let T = Int(readLine()!)!
    for _ in 0..<T {
        let n = Int(readLine()!)!
        
        let numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
        var visit = Array(repeating: false, count: n + 1)
        var sCount = 0
        
        for number in 1...numbers.count {
            if visit[number] {
                continue
            }
            
            var stack: Int? = number
            var pVisit = [Int]()
            
            while let node = stack {
                stack = nil
                visit[node] = true
                pVisit.append(node)
                if !visit[numbers[node - 1]] { //방문 없을때
                    stack = numbers[node - 1]
                } else { //방문 했을때
                    for pNode in pVisit {
                        if pNode == numbers[node - 1] {
                            break
                        }
                        sCount += 1
                    }
                }
            }
        }
        print(sCount)
    }
}

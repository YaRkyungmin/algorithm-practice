//
//  바이러스.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/04/22.
//

import Foundation

func 바이러스() {
    let computerCount = Int(readLine()!)!
    let edgeCount = Int(readLine()!)!
    var graph = Array(repeating: [Int](), count: computerCount + 1)
    var visit = Array(repeating: false, count: computerCount + 1)
    for _ in stride(from: 0, to: edgeCount, by: 1) {
        let input = readLine()!.split(separator: " ").compactMap { Int(String($0)) }
        graph[input[0]].append(input[1])
        graph[input[1]].append(input[0])
    }
    var stack = [1]
    visit[1] = true
    
    var result = 0
    
    while stack.count > 0 {
        let pop_virus = stack.popLast()!
        for i in graph[pop_virus] {
            if !visit[i] {
                visit[i] = true
                result += 1
                stack.append(i)
            }
        }
    }
    
    print(result)
}

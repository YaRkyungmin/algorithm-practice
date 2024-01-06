//
//  비숍.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/06.
//

import Foundation

func 비숍() {
    // 탐색수를 줄이는 것이 핵심인 문제
    let N = Int(readLine()!)!
    var gMap = [[Int]]()
    // 비숍 놓을 수 있는 곳 1, 비숍 놓을 수 없는 곳 0
    for _ in 0..<N {
        let row = readLine()!.split(separator: " ").compactMap { Int($0) }
        gMap.append(row)
    }
    // 대각선 oneList에 1인곳을 추가해 놓음
    var oneList = Array(repeating: [(Int, Int)](), count: 2 * N - 1)
    for y in 0..<N {
        for x in 0..<N {
            if gMap[y][x] == 1 {
                oneList[x + y].append((x, y))
            }
        }
    }
    
    var checkList = Array(repeating: false, count: 2 * N - 1)
    var result = 0
    
    func findBishop(max: Int, count: Int) { //우상향 대각선 번호, 비숍 놓은 횟수
        if max == 2 * N - 1{
            result = result < count ? count : result
            return
        }
        
        if oneList[max].count == 0 {
            findBishop(max: max + 1, count: count)
            return
        }
        
        var exeCount = 0
        
        for (x, y) in oneList[max] {
            let cConstant = x - y + N - 1
            if !checkList[cConstant] {
                exeCount += 1
                checkList[cConstant] = true
                findBishop(max: max + 1, count: count + 1)
                checkList[cConstant] = false
            }
        }
        
        if exeCount == 0 {
            findBishop(max: max + 1, count: count)
        }
    }
    
    findBishop(max: 0, count: 0)
    
    print(result)
}

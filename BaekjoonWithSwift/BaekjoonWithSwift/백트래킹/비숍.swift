//
//  비숍.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/06.
//

import Foundation

func 비숍() {
    let N = Int(readLine()!)!
    var gMap = [[Int]]()
    // 비숍 놓을 수 있는 곳 1, 비숍 놓을 수 없는 곳 0
    for _ in 0..<N {
        let row = readLine()!.split(separator: " ").compactMap { Int($0) }
        gMap.append(row)
    }
    // oneList에 1인곳을 추가해 놓음
    var oneList = [(Int, Int)]()
    for y in 0..<N {
        for x in 0..<N {
            if gMap[y][x] == 1 {
                oneList.append((x, y))
            }
        }
    }
    
    var aCheckList = Array(repeating: false, count: 2 * N - 1)
    var bCheckList = Array(repeating: false, count: 2 * N - 1)
    var checkList = Array(repeating: false, count: oneList.count)
    var result = 0
    
    func findBishop(max: Int) {
        if max == checkList.count {
            var cnt = 0
            for i in 0..<checkList.count {
                cnt += checkList[i] ? 1 : 0
            }
            result = result < cnt ? cnt : result
            return
        }
        
        var findCount = 0
        
        for i in max..<oneList.count {
            let node = oneList[i]
            let x = node.0
            let y = node.1
            let a = x + y
            let b = x - y + N - 1
            if !aCheckList[a] && !bCheckList[b] && !checkList[i] {
                findCount += 1
                checkList[i] = true
                aCheckList[a] = true
                bCheckList[b] = true
                findBishop(max: i + 1)
                checkList[i] = false
                aCheckList[a] = false
                bCheckList[b] = false
            }
        }
        
        if findCount == 0 {
            var cnt = 0
            for i in 0..<checkList.count {
                cnt += checkList[i] ? 1 : 0
            }
            result = result < cnt ? cnt : result
            return
        }
    }
    
    findBishop(max: 0)
    print(result)
}

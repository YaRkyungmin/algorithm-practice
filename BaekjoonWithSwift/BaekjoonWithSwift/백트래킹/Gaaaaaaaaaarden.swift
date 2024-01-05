//
//  Gaaaaaaaaaarden.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/05.
//

import Foundation

func Gaaaaaaaaaarden() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    let G = input[2]
    let R = input[3]
    var ground = [[Int]]()
    var twoGround = [(Int, Int)]()
    
    // 0은 호수 1은 배양액을 뿌릴 수 없는땅 2는 배양액을 뿌릴 수 있는 땅
    for _ in 0..<N {
        ground.append(readLine()!.split(separator: " ").compactMap { Int($0) })
    }
    // 배양액 뿌릴 수 있는 땅 모아 놓기
    for y in 0..<N {
        for x in 0..<M {
            if ground[y][x] == 2 {
                twoGround.append((x, y))
            }
        }
    }
    
    var setting = Array(repeating: 0, count: twoGround.count)
    var total = [[Int]]()
    // 배양액을 뿌리는 모든 경우의 수 구하기
    func spread(green: Int, red: Int, max: Int) {
        if green == 0 && red == 0 {
            // 그 경우를 저장
            total.append(setting)
            return
        }
        
        for i in max..<twoGround.count {
            if green > 0 {
                setting[i] = 1
                spread(green: green - 1, red: red, max: i + 1)
                setting[i] = 0
            }
            if red > 0 {
                setting[i] = 2
                spread(green: green, red: red - 1, max: i + 1)
                setting[i] = 0
            }
        }
    }
    
    spread(green: G, red: R, max: 0)
    var maxCount = 0
    
    while total.count > 0 {
        let patialSpread = total.popLast()!
        let result = bfsLiquid(sList: patialSpread)
        maxCount = maxCount < result ? result : maxCount
    }
    
    func bfsLiquid(sList: [Int]) -> Int {
        var queue = [(Int, Int, Int)]() // x, y, level
        var newGround = ground
        var visit = Array(repeating: Array(repeating: 0, count: M), count: N)
        
        for i in 0..<sList.count {
            let px = twoGround[i].0
            let py = twoGround[i].1
            
            if sList[i] == 1 {
                newGround[py][px] = 3
                queue.append((px, py, 0))
            } else if sList[i] == 2 {
                newGround[py][px] = 4
                queue.append((px, py, 0))
            } else {
                continue
            }
        }
        
        var pointer = 0
        let dx = [1, -1, 0, 0]
        let dy = [0, 0, 1, -1]
        var fCount = 0

        while pointer < queue.count {
            let node = queue[pointer]
            let x = node.0
            let y = node.1
            let level = node.2
            pointer += 1
            
            if newGround[y][x] == 5 {
                continue
            }
            
            for i in 0..<4 {
                let px = x + dx[i]
                let py = y + dy[i]
                
                if px >= 0 && px < M && py >= 0 && py < N && newGround[py][px] != 0 && newGround[py][px] != 5 {
                    if newGround[y][x] == 3 { //3 그린 일때
                        if newGround[py][px] == 4 && visit[py][px] == (level + 1) {
                            fCount += 1
                            newGround[py][px] = 5
                        } else if newGround[py][px] == 1 || newGround[py][px] == 2 {
                            queue.append((px, py, level + 1))
                            visit[py][px] = level + 1
                            newGround[py][px] = 3
                        }
                    } else { // 4 레드 일때
                        if newGround[py][px] == 3 && visit[py][px] == (level + 1) {
                            fCount += 1
                            newGround[py][px] = 5
                        } else if newGround[py][px] == 1 || newGround[py][px] == 2 {
                            queue.append((px, py, level + 1))
                            visit[py][px] = level + 1
                            newGround[py][px] = 4
                        }
                    }
                }
            }
        }
        
        return fCount
    }
    
    print(maxCount)
}

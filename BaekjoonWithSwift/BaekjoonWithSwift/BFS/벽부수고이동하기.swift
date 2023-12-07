//
//  벽부수고이동하기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/07.
//

import Foundation

func 벽부수고이동하기() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    var queue = [(Int, Int, Int)]()
    var pointer = 0
    var visit = Array(repeating: Array(repeating: [0,0], count:M), count: N)
    visit[0][0][0] = 1
    queue.append((0, 0, 0))
    var count = -1
    let dx = [-1, 1, 0 ,0]
    let dy = [0, 0, -1, 1]
    var gMap = [[Int]]()
    for _ in 0..<N {
        let row = Array(readLine()!).compactMap { Int(String($0)) }
        gMap.append(row)
    }

    while pointer <= (queue.count - 1) {
        let output = queue[pointer]
        pointer += 1
        
        let nx = output.0
        let ny = output.1
        let broken = output.2
        
        if ny == N-1 && nx == M-1 {
            count = visit[ny][nx][broken]
            break
        }

        for i in 0..<4 {
            let px = nx + dx[i]
            let py = ny + dy[i]
            if 0 > px || 0 > py || M == px || N == py || visit[py][px][broken] != 0 {
                continue
            } else {
                if gMap[py][px] == 1 && broken == 0 { // 벽일때
                    visit[py][px][1] = visit[ny][nx][0] + 1
                    queue.append((px, py, 1))
                } else if gMap[py][px] == 0 { // 벽아닐때
                    visit[py][px][broken] = visit[ny][nx][broken] + 1
                    queue.append((px, py, broken))
                }
            }
        }
    }

    print(count)
}



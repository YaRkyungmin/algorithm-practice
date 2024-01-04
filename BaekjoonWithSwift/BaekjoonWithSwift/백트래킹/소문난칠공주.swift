//
//  소문난칠공주.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/04.
//

import Foundation

func 소문난칠공주() {
    var cls = [[String]]()
    for _ in 0..<5 {
        cls.append(readLine()!.map {String($0)})
    }
    var arr = [(Int, Int)]()
    var visit = Array(repeating: false, count: 25)
    var count = 0
    func findSeven(k: Int, max: Int, Ycount: Int) {
        if k == 7 {
            if checkSom(student: arr) {
                count += 1
            }
            return
        }
        
        if Ycount >= 4 {
            return
        }
        
        for i in max..<25 {
            if !visit[i] {
                let y = i / 5
                let x = i % 5
                arr.append((x, y))
                visit[i] = true
                findSeven(k: k + 1, max: i + 1, Ycount: Ycount + (cls[y][x] == "Y" ? 1 : 0))
                arr.removeLast()
                visit[i] = false
            }
        }
    }

    func checkSom(student: [(Int, Int)]) -> Bool {
        var dVisit = Array(repeating: Array(repeating: false, count: 5), count: 5)
        var bVisit = Array(repeating: Array(repeating: false, count: 5), count: 5)
        var sCount = 0
        var cCount = 0
        let dx = [0, 0, -1, 1]
        let dy = [1, -1, 0, 0]
        // 7명 학생 위치 나타 내기
        for (x, y) in student {
            dVisit[y][x] = true
        }
        var queue = [(Int, Int)]()
        queue.append(student[0])
        var pointer = 0
        bVisit[student[0].1][student[0].0] = true
        
        while pointer < queue.count {
            let node = queue[pointer]
            pointer += 1
            
            let nx = node.0
            let ny = node.1
            sCount += cls[ny][nx] == "S" ? 1 : 0
            cCount += 1
            
            for i in 0..<4 {
                let px = nx + dx[i]
                let py = ny + dy[i]
                if 0 <= px && px < 5 && 0 <= py && py < 5 && dVisit[py][px] && !bVisit[py][px] {
                    queue.append((px, py))
                    bVisit[py][px] = true
                }
            }
        }
        return sCount >= 4 && cCount == 7 ? true : false
    }
    
    findSeven(k: 0, max: 0, Ycount: 0)
    print(count)
}

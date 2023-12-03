//
//  적록색약.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/04.
//

import Foundation

func 적록색약() {
    let N = Int(readLine()!)!
    var picture = [[String]]()

    for _ in 0..<N {
        picture.append(readLine()!.map { String($0) })
    }
    
    var stack = [[Int]]()
    
    var visit = Array(repeating: Array(repeating: 0, count: N), count: N)
    var oriCount = 0
    var bCount = 0
    
    let dx = [-1, 1, 0, 0]
    let dy = [0, 0, -1, 1]
    
    for y in 0..<N {
        for x in 0..<N {
            switch picture[y][x] {
            case "R":
                if visit[y][x] == 0 {
                    stack.append([x, y])
                    while stack.count > 0 {
                        let node = stack.popLast()!
                        visit[node[1]][node[0]] = 1
                        for i in 0..<4 {
                            if 0 <= node[1] + dy[i]
                                && node[1] + dy[i] < N
                                && 0 <= node[0] + dx[i]
                                && node[0] + dx[i] < N
                                && visit[node[1] + dy[i]][node[0] + dx[i]] == 0
                                && picture[node[1] + dy[i]][node[0] + dx[i]] == "R" {
                                stack.append([node[0] + dx[i], node[1] + dy[i]])
                            }
                        }
                    }
                    oriCount += 1
                }
            case "G":
                if visit[y][x] == 0 {
                    stack.append([x, y])
                    while stack.count > 0 {
                        let node = stack.popLast()!
                        visit[node[1]][node[0]] = 1
                        for i in 0..<4 {
                            if 0 <= node[1] + dy[i]
                                && node[1] + dy[i] < N
                                && 0 <= node[0] + dx[i]
                                && node[0] + dx[i] < N
                                && visit[node[1] + dy[i]][node[0] + dx[i]] == 0
                                && picture[node[1] + dy[i]][node[0] + dx[i]] == "G" {
                                stack.append([node[0] + dx[i], node[1] + dy[i]])
                            }
                        }
                    }
                    oriCount += 1
                }
            case "B":
                if visit[y][x] == 0 {
                    stack.append([x, y])
                    while stack.count > 0 {
                        let node = stack.popLast()!
                        visit[node[1]][node[0]] = 1
                        for i in 0..<4 {
                            if 0 <= node[1] + dy[i]
                                && node[1] + dy[i] < N
                                && 0 <= node[0] + dx[i]
                                && node[0] + dx[i] < N
                                && visit[node[1] + dy[i]][node[0] + dx[i]] == 0
                                && picture[node[1] + dy[i]][node[0] + dx[i]] == "B" {
                                stack.append([node[0] + dx[i], node[1] + dy[i]])
                            }
                        }
                    }
                    oriCount += 1
                    bCount += 1
                }
            default:
                continue
            }
        }
    }
    
    var xCount = 0
    for y in 0..<N {
        for x in 0..<N {
            switch picture[y][x] {
            case "R", "G":
                if visit[y][x] == 1 {
                    stack.append([x, y])
                    while stack.count > 0 {
                        let node = stack.popLast()!
                        visit[node[1]][node[0]] = 0
                        for i in 0..<4 {
                            if 0 <= node[1] + dy[i]
                                && node[1] + dy[i] < N
                                && 0 <= node[0] + dx[i]
                                && node[0] + dx[i] < N
                                && visit[node[1] + dy[i]][node[0] + dx[i]] == 1
                                && (picture[node[1] + dy[i]][node[0] + dx[i]] == "R" || picture[node[1] + dy[i]][node[0] + dx[i]] == "G") {
                                stack.append([node[0] + dx[i], node[1] + dy[i]])
                            }
                        }
                    }
                    xCount += 1
                }
            default:
                continue
            }
        }
    }
    
    print(oriCount, terminator: " ")
    print(xCount + bCount)
}

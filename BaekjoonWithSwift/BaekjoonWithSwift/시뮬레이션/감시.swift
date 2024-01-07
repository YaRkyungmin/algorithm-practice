//
//  감시.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/07.
//

import Foundation

func 감시() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let M = input[1]
    var office = [[Int]]()
    for _ in 0..<N {
        let row = readLine()!.split(separator: " ").compactMap { Int($0) }
        office.append(row)
    }
    
    var cctvList = [(Int, Int)]()
    findCCTV()
    
    func findCCTV() {
        for y in 0..<N {
            for x in 0..<M {
                if office[y][x] != 0 && office[y][x] != 6 { //CCTV일때
                    cctvList.append((x, y))
                }
            }
        }
    }
    
    var result = 1000000
    // 완전 탐색
    var typeList = Array(repeating: 0, count: cctvList.count)
    findBlindSpot(max: 0)
    print(result)
    
    func findBlindSpot(max: Int) {
        if max == cctvList.count {
            var newOffice = office
            setupOffice()
            let blindSpot = countBlindSpot()
            result = result > blindSpot ? blindSpot : result
            
            func countBlindSpot() -> Int {
                var c = 0
                
                for y in 0..<N {
                    for x in 0..<M {
                        if newOffice[y][x] == 0 {
                            c += 1
                        }
                    }
                }
                
                return c
            }
            
            func setupOffice() {
                for (i, (x, y)) in cctvList.enumerated() {
                    let cctvNumber = office[y][x]
                    switch cctvNumber {
                    case 1:
                        switch typeList[i] {
                        case 1:
                            right(x: x, y: y)
                        case 2:
                            bottom(x: x, y: y)
                        case 3:
                            left(x: x, y: y)
                        case 4:
                            top(x: x, y: y)
                        default:
                            return
                        }
                    case 2:
                        switch typeList[i] {
                        case 1:
                            right(x: x, y: y)
                            left(x: x, y: y)
                        case 2:
                            bottom(x: x, y: y)
                            top(x: x, y: y)
                        default:
                            return
                        }
                    case 3:
                        switch typeList[i] {
                        case 1:
                            top(x: x, y: y)
                            right(x: x, y: y)
                        case 2:
                            right(x: x, y: y)
                            bottom(x: x, y: y)
                        case 3:
                            bottom(x: x, y: y)
                            left(x: x, y: y)
                        case 4:
                            left(x: x, y: y)
                            top(x: x, y: y)
                        default:
                            return
                        }
                    case 4:
                        switch typeList[i] {
                        case 1:
                            top(x: x, y: y)
                            right(x: x, y: y)
                            left(x: x, y: y)
                        case 2:
                            top(x: x, y: y)
                            right(x: x, y: y)
                            bottom(x: x, y: y)
                        case 3:
                            right(x: x, y: y)
                            bottom(x: x, y: y)
                            left(x: x, y: y)
                        case 4:
                            top(x: x, y: y)
                            bottom(x: x, y: y)
                            left(x: x, y: y)
                        default:
                            return
                        }
                    case 5:
                        top(x: x, y: y)
                        right(x: x, y: y)
                        bottom(x: x, y: y)
                        left(x: x, y: y)
                    default:
                        return
                    }
                    
                }
                
                func left(x: Int, y: Int) {
                    //1 왼쪽으로 줄어들기
                    var cX = x - 1
                    
                    while cX >= 0 && newOffice[y][cX] != 6 {
                        if newOffice[y][cX] == 0 {
                            newOffice[y][cX] = -1
                        }
                        cX -= 1
                    }
                }
                
                func right(x: Int, y: Int) {
                    //2 오른쪽으로 커지기
                    var cX = x + 1
                    
                    while cX < M && newOffice[y][cX] != 6 {
                        if newOffice[y][cX] == 0 {
                            newOffice[y][cX] = -1
                        }
                        cX += 1
                    }
                }
                
                func top(x: Int, y: Int) {
                    //3 위로 줄어들기
                    var cY = y - 1
                    
                    while cY >= 0 && newOffice[cY][x] != 6 {
                        if newOffice[cY][x] == 0 {
                            newOffice[cY][x] = -1
                        }
                        cY -= 1
                    }
                }
                
                func bottom(x: Int, y: Int) {
                    //4 아래로 커지기
                    var cY = y + 1
                    
                    while cY < N && newOffice[cY][x] != 6 {
                        if newOffice[cY][x] == 0 {
                            newOffice[cY][x] = -1
                        }
                        cY += 1
                    }
                }
            }
            
            return
        }
        
        let cctvPoint = cctvList[max]
        let x = cctvPoint.0
        let y = cctvPoint.1
        let cctvNumber = office[y][x]
        
        switch cctvNumber {
        case 1:
            for i in 1...4 {
                typeList[max] = i
                findBlindSpot(max: max + 1)
            }
        case 2:
            for i in 1...2 {
                typeList[max] = i
                findBlindSpot(max: max + 1)
            }
        case 3:
            for i in 1...4 {
                typeList[max] = i
                findBlindSpot(max: max + 1)
            }
        case 4:
            for i in 1...4 {
                typeList[max] = i
                findBlindSpot(max: max + 1)
            }
        case 5:
            typeList[max] = 1
            findBlindSpot(max: max + 1)
        default:
            return
        }
    }
}

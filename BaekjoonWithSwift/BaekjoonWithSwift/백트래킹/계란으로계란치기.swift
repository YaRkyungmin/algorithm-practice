//
//  계란으로계란치기.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/01/04.
//

import Foundation

func 계란으로계란치기() {
    let N = Int(readLine()!)!
    var sBasket = [Int]()
    var wBasket = [Int]()
    for _ in 0..<N {
        let input = readLine()!.split(separator: " ").compactMap { Int($0) }
        let S = input[0]
        let W = input[1]
        sBasket.append(S)
        wBasket.append(W)
    }
    var broken = Array(repeating: false, count: N)
    var maxCount = 0
    
    func hitEgg(hitNum: Int) {
        if hitNum == N {
            var bCount = 0
            for i in broken {
                bCount += i ? 1 : 0
            }
            maxCount = maxCount < bCount ? bCount : maxCount
            
            return
        }
        
        if broken[hitNum] {
            hitEgg(hitNum: hitNum + 1)
            return
        }
        
        var bCount = 0
        for i in broken {
            bCount += !i ? 1 : 0
        }
        if bCount == 1 {
            hitEgg(hitNum: hitNum + 1)
            return
        }
        
        for i in 0..<N {
            if hitNum == i || broken[i] {
                continue
            }
            
            sBasket[hitNum] -= wBasket[i]
            sBasket[i] -= wBasket[hitNum]
            
            if sBasket[hitNum] <= 0 {
                broken[hitNum] = true
            }
            if sBasket[i] <= 0 {
                broken[i] = true
            }
            
            hitEgg(hitNum: hitNum + 1)
            
            if sBasket[hitNum] <= 0 {
                broken[hitNum] = false
            }
            if sBasket[i] <= 0 {
                broken[i] = false
            }
            
            sBasket[hitNum] += wBasket[i]
            sBasket[i] += wBasket[hitNum]
        }
    }
    
    hitEgg(hitNum: 0)
    print(maxCount)
}

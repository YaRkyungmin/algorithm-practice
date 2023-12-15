//
//  Z.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/12/15.
//

import Foundation

func Z() {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = input[0]
    let r = input[1]
    let c = input[2]

    func zSearch(n: Int, r: Int, c: Int) -> Int {
        if n == 0 {
            return 0
        }
        // r이 y좌표 c이 x좌표
        if r < 1<<(n-1) && c < 1<<(n-1) { //1사분면
            return zSearch(n: n-1, r: r, c: c)
        } else if r < 1<<(n-1) && 1<<(n-1) <= c { //2사분면
            return (1<<(2*n-2)) + zSearch(n: n - 1, r: r, c: c - 1<<(n-1))
        } else if 1<<(n-1) <= r && c < 1<<(n-1) { //3사분면
            return (1<<(2*n-2)) * 2 + zSearch(n: n - 1, r: r - 1<<(n-1), c: c)
        } else { //4사분면
            return (1<<(2*n-2)) * 3 + zSearch(n: n - 1, r: r - 1<<(n-1), c: c - 1<<(n-1))
        }
    }
    print(zSearch(n: N, r: r, c: c))
}

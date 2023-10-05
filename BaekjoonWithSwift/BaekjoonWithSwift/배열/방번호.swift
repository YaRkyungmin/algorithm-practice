//
//  방번호.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func 방번호() {
    let input = readLine() ?? "0"

    var array = Array(repeating: 0, count: 10)

    for i in input {
        if i == "9" {
            if array[9] > array[6] {
                array[6] += 1
            } else {
                array[9] += 1
            }
        } else if i == "6" {
            if array[9] < array[6] {
                array[9] += 1
            } else {
                array[6] += 1
            }
        } else {
            array[Int(String(i)) ?? 0] += 1
        }
    }
}

//
//  괄호의값.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/27.
//

import Foundation

func 괄호의값() {
    let input = readLine()!.map { String($0) }
    var totalSum = 0
    var partialSum = 1
    var stack = [String]()
    var signal = false

    for i in (0..<input.count).reversed() {
        var breakSignal = false

        switch input[i] {
        case ")":
            if signal {
                totalSum += stack.reduce(partialSum) {
                    switch $1 {
                    case ")":
                        return $0 * 2
                    case "]":
                        return $0 * 3
                    default:
                        return 0
                    }
                }
                partialSum = 1
                signal = false
            }
            
            stack.append(")")
        case "]":
            if signal {
                totalSum += stack.reduce(partialSum) {
                    switch $1 {
                    case ")":
                        return $0 * 2
                    case "]":
                        return $0 * 3
                    default:
                        return 0
                    }
                }
                partialSum = 1
                signal = false
            }
            
            stack.append("]")
        case "(":
            if stack.count > 0 && stack.popLast()! == ")" {

                partialSum *= 2
                signal = true
                if stack.count == 0 {
                    totalSum += partialSum
                    partialSum = 1
                    signal = false
                }

            } else {
                totalSum = 0
                breakSignal = true
            }
        case "[":
            if stack.count > 0 && stack.popLast()! == "]" {

                partialSum *= 3
                signal = true
                if stack.count == 0 {
                    totalSum += partialSum
                    partialSum = 1
                    signal = false
                }

            } else {
                totalSum = 0
                breakSignal = true
            }
        default:
            continue
        }

        if breakSignal {
            break
        }
    }


    print(stack.count == 0 ? totalSum : 0)
}

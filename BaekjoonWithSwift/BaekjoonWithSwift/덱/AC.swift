//
//  AC.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/22.
//

import Foundation

func AC() {
    let T = Int(readLine()!)!
    
    for _ in 0..<T {
        let command = readLine()!
        let len = Int(readLine()!)!
        
        var inputArr = readLine()!
        inputArr.removeFirst()
        inputArr.removeLast()
        
        let numbers = inputArr.split(separator: ",").map{Int(String($0))!}
        
        var head = 0
        var tail = len - 1
        var signal = true
        var errorSiganl = false
        
        for i in command {
            switch String(i) {
            case "R":
                signal = signal ? false : true
            case "D":
                if head > tail {
                    errorSiganl = true
                    break
                }
                if signal {
                    head += 1
                } else {
                    tail -= 1
                }
            default:
                continue
            }
        }
        
        if errorSiganl {
            print("error")
        } else {
            if head > tail {
                print("[]")
            } else {
                if signal {
                    print("[", terminator: "")
                    print(numbers[head...tail].compactMap { String($0) }.joined(separator: ","), terminator: "")
                    print("]")
                } else {
                    print("[", terminator: "")
                    var output = [String]()
                    for i in (head...tail).reversed() {
                        output.append(String(numbers[i]))
                    }
                    print(output.joined(separator: ","), terminator: "")
                    print("]")
                }
            }
        }
    }
}

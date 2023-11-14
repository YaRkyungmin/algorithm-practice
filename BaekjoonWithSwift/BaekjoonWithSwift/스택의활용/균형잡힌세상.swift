//
//  균형잡힌세상.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2023/11/27.
//

import Foundation

func 균형잡힌세상() {
    while true {
        var input = readLine()!
        var stack1 = [String]()
        var signal = true
        
        if input == "." {
            break
        }
        
        while input.count > 0 {
            let ele = String(input.popLast()!)
            switch ele {
            case "(":
                if stack1.count > 0 {
                    if String(stack1.popLast()!) != ")" {
                        signal = false
                        break
                    }
                } else {
                    signal = false
                    break
                }
            case ")":
                stack1.append(ele)
            case "[":
                if stack1.count > 0 {
                    if String(stack1.popLast()!) != "]" {
                        signal = false
                        break
                    }
                } else {
                    signal = false
                    break
                }
            case "]":
                stack1.append(ele)
                
            default:
                continue
            }
        }
        
        if stack1.count > 0 {
            signal = false
        }
        
        print(signal ? "yes" : "no")
    }
}

//
//  DFS와BFS.swift
//  BaekjoonWithSwift
//
//  Created by kyungmin on 2024/04/29.
//

import Foundation

func DFS와BFS() {
    let input = readLine()!.split(separator: " ").compactMap { Int(String($0)) }
    let N = input[0]
    let M = input[1]
    let V = input[2]
    
    var graph = Array(repeating: [Int](), count: N + 1)
    var visit = Array(repeating: false, count: N + 1)
    
    for _ in stride(from: 0, to: M, by: 1) {
        let edge = readLine()!.split(separator: " ").compactMap { Int(String($0)) }
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    }
    
    var visitDfs = [String]()
    
    func dfs() {
        var stack = [V]
        while stack.count > 0 {
            let popNode = stack.popLast()!
            if visit[popNode] == false {
                visitDfs.append(String(popNode))
                visit[popNode] = true
            }
            var visitNode = graph[popNode].sorted()
            visitNode.reverse()
            for i in visitNode {
                if visit[i] == false {
                    stack.append(i)
                }
            }
        }
    }
    
    var visitBfs = [String]()
    var newVisit = Array(repeating: false, count: N + 1)
    
    func bfs() {
        var pointer = 0
        var queue = [V]
        while pointer < queue.count {
            let popNode = queue[pointer]
            pointer += 1
            if newVisit[popNode] == false {
                visitBfs.append(String(popNode))
                newVisit[popNode] = true
            }
            let visitNode = graph[popNode].sorted()
            for i in visitNode {
                if newVisit[i] == false {
                    queue.append(i)
                }
            }
        }
    }
    
    dfs()
    bfs()
    
    print(visitDfs.joined(separator: " "))
    print(visitBfs.joined(separator: " "))
}

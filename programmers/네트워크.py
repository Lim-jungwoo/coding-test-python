from collections import defaultdict

def solution(n, computers):
    # 무방향 그래프로 연결
    graph = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    
    # dfs로 들어가면서 연결되어 있는지 확인한다.
    # 연결되지 않은 노드도 모두 확인할 수 있어야 한다.
    # visited로 방문했는지 확인한다.
    visited = [False] * n
    
    def dfs(computer):
        visited[computer] = True
        next_computer = graph[computer]
        
        if not next_computer:
            return
        
        for i, _ in enumerate(next_computer):
            if not visited[next_computer[i]]:
                dfs(next_computer[i])
        
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer
    
    
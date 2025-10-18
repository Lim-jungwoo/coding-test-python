def solution(n, wires):
    from collections import defaultdict, deque
    
    graph = defaultdict(set)
    for a, b in wires:
        graph[a].add(b)
        graph[b].add(a)
    
    def bfs(start):
        visited = set([start])
        q = deque([start])
        while q:
            curr = q.popleft()
            for next in graph[curr]:
                if next not in visited:
                    visited.add(next)
                    q.append(next)
        return len(visited)
    
    answer = float('inf')
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        diff = abs(bfs(a) - bfs(b))
        answer = min(answer, diff)
        
        graph[a].add(b)   # 복원
        graph[b].add(a)   # 복원
        
    return answer

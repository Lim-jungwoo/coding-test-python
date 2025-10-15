from collections import deque
def solution():
    N, M = map(int, input().split())
    graph = {}
    indegrees = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        if graph.get(a):
            graph[a].append(b)
        else:
            graph[a] = [b]
        indegrees[b] += 1

    q = deque()
    # 진입차수가 0인 노드 모두 집어넣기
    for i, indegree in enumerate(indegrees):
        if i != 0 and indegree == 0:
            q.append(i)

    # 진입차수 0인 노드부터 빼기
    answer = []
    while q:
        curr = q.popleft()
        answer.append(curr)

        if graph.get(curr):
            for i, _ in enumerate(graph[curr]):
                next = graph[curr][i]
                indegrees[next] -= 1
                if indegrees[next] == 0: q.append(next)
    
    print(' '.join(map(str, answer)))
        
if __name__ == '__main__':
    solution()
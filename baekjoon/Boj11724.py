from collections import defaultdict, deque
import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = defaultdict(list)
    visited = [False] * (N + 1)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        q = deque([start])
        visited[start] = True
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

    count = 0
    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
            count += 1

    print(count)

if __name__ == '__main__':
    solution()

from collections import deque

def solution():
    M, N = map(int, input().split())
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[False] * M for _ in range(N)]

    tomatoes = []
    zero_count = 0
    q = deque()
    for n in range(N):
        tomatoes.append(list(map(int, input().split())))
        for m in range(M):
            if tomatoes[n][m] == 0:
                zero_count += 1
            elif tomatoes[n][m] == 1:
                q.append((n, m))
                visited[n][m] = True

    answer = 0
    tmp_q = deque()
    while q:
        curr = q.popleft()

        for dx, dy in dirs:
            nx = curr[0] + dx
            ny = curr[1] + dy
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and tomatoes[nx][ny] == 0:
                tmp_q.append((nx, ny))
                zero_count -= 1
                visited[nx][ny] = True

        if not q:
            if not tmp_q:
                break
            answer += 1
            while tmp_q:
                q.append(tmp_q.popleft())

    if zero_count != 0:
        return -1

    return answer

if __name__ == '__main__':
    print(solution())
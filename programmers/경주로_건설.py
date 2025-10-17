from collections import deque

def solution(board):
    n = len(board)
    # 아래쪽, 오른쪽, 위쪽, 왼쪽
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # 4방향마다 칸의 비용
    cost = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    # x, y, 방향, 비용
    q = deque()
    q.append((0, 0, 0, 0))
    cost[0][0][0] = 0
    q.append((0, 0, 1, 0))
    cost[0][0][1] = 0
    
    while q:
        x, y, dir, c = q.popleft()
        for ndir, (dx, dy) in enumerate(dirs):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                nc = c + (100 if dir == ndir else 600)
                if cost[nx][ny][ndir] > nc:
                    cost[nx][ny][ndir] = nc
                    q.append((nx, ny, ndir, nc))
                    
    return min(cost[-1][-1])
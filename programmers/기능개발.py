from collections import deque
import math

def solution(progresses, speeds):
    q = deque()
    # 남은 기간을 넣어두고, 먼저 뺀 값보다 작은 값들은 다 뺀다.
    for i in range(len(progresses)):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    answer = []
    while q:
        count = 1
        curr = q.popleft()
        while q and q[0] <= curr:
            q.popleft()
            count += 1
        answer.append(count)
    return answer
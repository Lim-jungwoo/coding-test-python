def solution(tickets):
    n = len(tickets)
    tickets.sort()  # 사전순 정렬

    def dfs(path, used):
        if len(used) == n:
            return path

        for i in range(n):
            if i in used:
                continue
            if tickets[i][0] == path[-1]:
                # 매 탐색마다 새로운 복사본 생성
                result = dfs(path + [tickets[i][1]], used + [i])
                if result:
                    return result
        return False

    return dfs(["ICN"], [])

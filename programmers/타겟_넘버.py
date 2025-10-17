def solution(numbers, target):
    # 하나씩 부호를 정해서 값을 구한다.
    n = len(numbers)
    answer = 0
    
    def dfs(idx, val):
        nonlocal answer
        
        if idx == n:
            if val == target:
                answer += 1
            return
        
        # 더하기
        dfs(idx + 1, val + numbers[idx])
        # 빼기
        dfs(idx + 1, val - numbers[idx])
        
    dfs(0, 0)
    return answer
        
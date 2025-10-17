def solution(N, number):
    # 최솟값이 8보다 크면 -1을 return
    # 1. 숫자를 i번 사용했을 경우의 모든 값을 저장한다.
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # 사칙연산 수행
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    dp[i].add(k + l)
                    dp[i].add(k - l)
                    dp[i].add(k * l)
                    if l != 0 and k != 0: dp[i].add(k // l)
        if number in dp[i]: return i
    
    return -1
def solution(triangle):
    # 숫자의 합이 가장 큰 경우
    # dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[j]
    triangle_len = len(triangle)
    dp = [[0] * i for i in range(1, triangle_len + 1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, triangle_len):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                
    return max(dp[triangle_len - 1])
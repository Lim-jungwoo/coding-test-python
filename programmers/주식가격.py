from collections import deque

def solution(prices):
    stack = deque()
    
    answer = [0] * len(prices)
    for time, price in enumerate(prices):
        while stack and stack[-1][0] > price:
            p, t = stack.pop()
            answer[t] = time - t
        stack.append((price, time))
    
    while stack:
        p, t = stack.pop()
        answer[t] = len(prices) - 1 - t
    
    return answer
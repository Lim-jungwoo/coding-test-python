def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:  # 짝수면 그냥 +1
            answer.append(n + 1)
        else:
            # (x ^ (x + 1)) >> 2 + 1 이 정답과의 차이
            answer.append(n + ((n ^ (n + 1)) >> 2) + 1)
    return answer

def solution(brown, yellow):
    total = brown + yellow

    for y in range(3, total + 1):
        if total % y == 0:  # 나누어 떨어질 때만
            x = total // y
            if (x - 2) * (y - 2) == yellow:
                return [x, y]  # 가로가 더 크거나 같음

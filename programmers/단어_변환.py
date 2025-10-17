from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0  # target이 words에 없으면 불가능

    visited = [False] * len(words)

    def can_transform(a, b):
        """두 단어가 한 글자만 다르면 True"""
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    q = deque([(begin, 0)])  # (단어, 변환 단계 수)

    while q:
        curr, steps = q.popleft()
        if curr == target:
            return steps

        for i, word in enumerate(words):
            if not visited[i] and can_transform(curr, word):
                visited[i] = True
                q.append((word, steps + 1))

    return 0

from collections import deque

def solution(p):
    # 균형잡힌 괄호 문자열로 분리
    def split_str(line):
        left_count = 0
        right_count = 0
        for index, ch in enumerate(line):
            if ch == '(':
                left_count += 1
            elif ch == ')':
                right_count += 1
            if left_count == right_count:
                return line[:index+1], line[index+1:]
        return line
        
    
    # 올바른 괄호 문자열인지 확인
    def is_right(line):
        stack = deque()
        
        for ch in line:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if not stack:
                    return False
                stack.pop()
        return True
    
    # 1. 빈 문자열인 경우, 빈 문자열 반환
    # 2. 문자열을 u, v로 분리
    # 3. u가 올바른 괄호 문자열인지 확인
    # 4. u를 올바른 문자열로 수정
    # 4-1. 빈 문자열에 첫 번째 문자로 (를 붙인다
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
    # 4-3. )를 붙인다.
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
    # 4-5. 생성된 문자열을 반환한다.
    def dfs(line):
        if is_right(line):
            return line
        
        u, v = split_str(line)
        # u가 올바른 문자열일 때
        if is_right(u):
            return u + dfs(v)
        # u를 올바른 문자열로 수정
        else:
            arr = ['(']
            for ch in dfs(v):
                arr.append(ch)
            arr.append(')')
            u = u[1:-1]
            for ch in u:
                if ch == '(':
                    arr.append(')')
                elif ch == ')':
                    arr.append('(')
            u = ''.join(arr)
        return u
    
    return dfs(p)
    
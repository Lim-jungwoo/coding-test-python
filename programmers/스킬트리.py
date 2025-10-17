def solution(skill, skill_trees):
    # skill 순서대로 가는 지만 확인하면 된다
    answer = 0
    dict = {}
    for i, ch in enumerate(skill):
        dict[ch] = i
    
    for skill_tree in skill_trees:
        prev = 0
        is_valid = True
        for ch in skill_tree:
            if ch in dict:
                if prev != dict.get(ch):
                    is_valid = False
                    break
                prev += 1
        if is_valid:
            answer += 1
    return answer
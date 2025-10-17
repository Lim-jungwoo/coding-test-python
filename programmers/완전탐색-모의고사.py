def solution(answers):
    one = [1, 2, 3, 4, 5]
    one_len = len(one)
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    two_len = len(two)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    three_len = len(three)
    
    counts = [0] * 3
    for i, answer in enumerate(answers):
        one_index = i % one_len
        two_index = i % two_len
        three_index = i % three_len
        if answer == one[one_index]:
            counts[0] += 1
        if answer == two[two_index]:
            counts[1] += 1
        if answer == three[three_index]:
            counts[2] += 1
    
    max_count = max(counts)
    result = []
    for i, count in enumerate(counts):
        if max_count == count:
            result.append(i + 1)
            
    return result

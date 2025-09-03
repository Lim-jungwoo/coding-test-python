
def main():
    N, M, K = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))

    nums.sort(reverse=True)
    first_max_num = nums[0]
    second_max_num = nums[1]

    result1 = 0
    # 1) 반복문으로 풀기
    for i, count in enumerate(range(M), start=1):
        if i % (K + 1) == 0:
            result1 += second_max_num
        else:
            result1 += first_max_num

    # 2) 수열로 풀기
    first_max_count = int(M / (K + 1)) * K
    first_max_count += M % (K + 1)
    result2 = 0
    result2 += (first_max_count) * first_max_num        # 가장 큰 수 더하기
    result2 += (M - first_max_count) * second_max_num   # 2번째로 큰 수 더하기
    
    print(result1)
    print(result2)

    


if __name__ == '__main__':
    main()
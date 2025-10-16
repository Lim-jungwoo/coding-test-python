import sys
input = sys.stdin.readline

# 사용량 → 요금
def bill_from_wh(wh: int) -> int:
    if wh <= 100:
        return wh * 2
    elif wh <= 10_000:
        return 100 * 2 + (wh - 100) * 3
    elif wh <= 1_000_000:
        return 100 * 2 + 9_900 * 3 + (wh - 10_000) * 5
    else:
        return 100 * 2 + 9_900 * 3 + 990_000 * 5 + (wh - 1_000_000) * 7

# 요금 → 사용량 (역함수)
def wh_from_bill(bill: int) -> int:
    # 누적 요금 임계치
    # 첫 100 Wh 요금: 100*2 = 200
    # 다음 9,900 Wh 요금: 9,900*3 = 29,700
    # 다음 990,000 Wh 요금: 990,000*5 = 4,950,000
    # 누적 임계 요금들:
    thresh1 = 100 * 2
    thresh2 = thresh1 + 9_900 * 3
    thresh3 = thresh2 + 990_000 * 5

    if bill <= thresh1:
        return bill // 2
    elif bill <= thresh2:
        # 이미 요금 200 쓴 뒤 나머지를 3원/Wh 계산
        return 100 + (bill - thresh1) // 3
    elif bill <= thresh3:
        return 10_000 + (bill - thresh2) // 5
    else:
        return 1_000_000 + (bill - thresh3) // 7

def solve():
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break

        # 둘이 쓴 전기량의 합
        total_wh = wh_from_bill(A)

        # 상근이가 쓴 전기량은 0 ~ total_wh 범위지만,
        # 조건에 따라 탐색 범위를 좁힐 수 있음.
        # 상근이 요금 < 이웃 요금이므로 mid ≤ total_wh//2 가능
        low, high = 0, total_wh // 2

        while low <= high:
            mid = (low + high) // 2
            my_wh = mid
            nei_wh = total_wh - mid

            my_bill = bill_from_wh(my_wh)
            nei_bill = bill_from_wh(nei_wh)

            diff = nei_bill - my_bill  # 항상 이웃 요금이 더 크거나 같음 (상근이가 덜 썼기 때문)

            if diff == B:
                # 이 경우가 정답
                print(my_bill)
                break
            elif diff > B:
                # 요금 차가 더 크다 → 내 사용량을 늘려야 함 (내 요금 ↑, 차이 ↓)
                low = mid + 1
            else:
                # 차가 작다 → 내 사용량 줄여야 함 (내 요금 ↓, 차이 ↑)
                high = mid - 1

if __name__ == "__main__":
    solve()

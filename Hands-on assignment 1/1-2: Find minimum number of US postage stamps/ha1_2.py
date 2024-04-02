def greedy_stamp_finder(stamp_prices, target_amount):
    """
    그리디 알고리즘으로 목표 금액에 도달하기 위해 필요한 최소한의 우표 개수를 찾기
    이 함수는 우표 가격이 서로 다르다고 가정

    매개변수:
    stamp_prices (list): 서로 다른 우표 가격 목록
    target_amount (int): 도달하려는 목표 우표 비용

    반환값:
    list: 목표 금액을 만드는 데 사용된 우표 가격 목록 (반드시 최적은 아님)
    """

    # 우표 가격을 내림차순으로 정렬하여 최고 가치 우표부터 시작
    sorted_stamps = sorted(stamp_prices, reverse=True)
    used_stamps = []  # 사용된 우표를 저장할 목록
    remaining_amount = target_amount  # 목표 금액에 도달하기 위해 남은 금액

    # 정렬된 우표 가격 목록을 순회
    for stamp in sorted_stamps:
        # 남은 금액이 우표 가격보다 클 때까지 현재 우표를 가능한 많이 사용
        while remaining_amount >= stamp:
            remaining_amount -= stamp  # 남은 금액에서 우표 가격을 차감
            used_stamps.append(stamp)  # 우표를 사용된 우표 목록에 추가
    
    return used_stamps

# 제공된 우표 가격과 목표 금액으로 함수를 호출
used_stamps = greedy_stamp_finder([1, 10, 21, 34, 70, 100, 350, 1225, 1500], 140)

# 함수 실행 결과를 나타내기 위해 사용된 우표를 출력
print(used_stamps)
# 사용된 우표 결과 : [100, 34, 1, 1, 1, 1, 1, 1]
print(len(used_stamps))
# 사용된 우표 개수 : 8장

"""
import sys     

input_stamps = list(map(int,sys.stdin.readline().split()))
cost = int(sys.stdin.readline())

used_stamps = greedy_stamp_finder(input_stamps,cost)

print(used_stamps)
print(len(used_stamps))
"""

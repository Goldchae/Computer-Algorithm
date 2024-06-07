'''
min_stamps 메서드
주어진 우표 목록과 총 금액에 대해, 필요한 최소 우표 개수를 동적 계획법을 이용해 계산하는 함수입니다.
'''
def min_stamps(coins, amount):
    dp = [float('inf')] * (amount + 1)  # 각 금액별 필요한 최소 우표 개수를 저장할 배열
    dp[0] = 0 # 0원을 만드는 데 필요한 우표 개수는 0개
    
    # 각 우표 금액별로 가능한 모든 금액을 업데이트
    for coin in coins:
        # 우표 금액으로부터 총 금액까지 순회하며 최소 우표 개수 업데이트
        for i in range(coin, amount + 1):
            # 기존의 개수와 비교하여 더 적은 우표 개수를 선택
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] # 요구 금액을 만드는 데 필요한 최소 우표 개수 반환


### 테스트 코드
postage_stamps = [1, 10, 21, 34, 70, 100, 350, 1225, 1500]
postage_amount = 140
result = min_stamps(postage_stamps, postage_amount)
print(result)  # 최소 우표 개수 출력


### 사용자 입력용 코드
# import sys
# input = sys.stdin.readline
# postage_stamps = list(map(int,input().split()))
# postage_amount = int(input())
# result = min_stamps(postage_stamps, postage_amount)
# print(result)

'''
lis() 메서드
이 함수는 주어진 배열에서 가장 긴 증가하는 부분 수열(LIS)을 찾아 그 길이와 원소들을 반환합니다.
'''
def lis(arr):
    n = len(arr) # 입력 배열의 길이를 n에 저장
    h = [1] * n  # h 리스트를 초기화, 각 요소는 해당 위치까지의 최대 LIS 길이를 나타냄
    prev_index = [-1] * n # 이전 요소의 인덱스를 추적하기 위한 리스트
    
    # 전체 배열을 순회하면서 각 요소를 비교하여 LIS 계산
    for i in range(1, n):
        for j in range(0, i):
            # 현재 요소가 이전 요소보다 크고 이전 요소의 LIS 길이 + 1이 현재 요소의 LIS 길이보다 클 때
            if arr[i] > arr[j] and h[i] < h[j] + 1:
                # 최대 길이와 이전 인덱스 업데이트
                h[i] = h[j] + 1
                prev_index[i] = j

    # h 리스트에서 최대 길이 추출
    max_len = max(h) # 최대 LIS 길이
    max_len_index = h.index(max_len) # 최대 길이의 인덱스

    lis = [] # 결과 LIS를 저장할 리스트
    # prev_index를 사용해 LIS를 역순으로 추적
    while max_len_index != -1:
        lis.append(arr[max_len_index])
        max_len_index = prev_index[max_len_index]
    
    lis.reverse() # 추적한 순서를 뒤집어 원래 순서로 복원
    
    return lis, max_len # LIS와 그 길이 반환


### 테스트 코드
arr = [10, 22, 9, 33, 21, 50, 41, 60]
LIS, LIS_length = lis(arr)
print(LIS) # 출력: [10, 22, 33, 50, 60]
print(LIS_length) # 출력: 5



### 사용자 입력용 코드
# import sys
# input = sys.stdin.readline
# arr = list(map(int,input().split()))
# LIS, LIS_length = lis(arr)
# print(LIS)
# print(LIS_length)

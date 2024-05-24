import time # 시간 비교용
start = time.time()

def partition(arr, low, high):
    """
    분할 함수는 배열의 마지막 원소를 피벗으로 사용하고, 피벗을 올바른 정렬 위치에 배치하며,
    피벗보다 작은 모든 원소를 피벗의 왼쪽에, 큰 원소를 오른쪽에 배치
    """
    pivot = arr[high]  # 피벗은 배열의 마지막 원소
    i = low - 1  # 더 작은 원소의 인덱스
    
    for j in range(low, high):  # 낮은 인덱스부터 높은 인덱스 - 1까지 반복
        if arr[j] < pivot:  # 현재 원소가 피벗보다 작다면
            i = i + 1  # 더 작은 원소의 인덱스를 증가
            arr[i], arr[j] = arr[j], arr[i]  # 인덱스 i와 j에 있는 원소를 교환
    arr[i+1], arr[high] = arr[high], arr[i+1]  # 피벗 원소를 인덱스 i+1에 있는 원소와 교환
    return i + 1  # 분할 인덱스를 반환


def optimized_quicksort(arr, low, high):
    """
    퀵 정렬을 구현하는 메인 함수
    """
    if low < high:  # 낮은 인덱스가 높은 인덱스보다 작다면
        # pi는 분할 인덱스이며, arr[pi]는 이제 올바른 위치에 있음
        pi = partition(arr, low, high)
        
        # 분할 인덱스 전과 후의 원소들을 각각 정렬
        optimized_quicksort(arr, low, pi-1)  # 분할 인덱스 이전의 부분 배열에 대해 재귀적으로 퀵 정렬을 적용
        optimized_quicksort(arr, pi+1, high)  # 분할 인덱스 이후의 부분 배열에 대해 재귀적으로 퀵 정렬을 적용


# 예제 배열
example_array = [21, 3, 12, 15, 7, 32, 4, 25, 9, 18]
optimized_quicksort(example_array, 0, len(example_array)-1)
print(example_array)
## [3, 4, 7, 9, 12, 15, 18, 21, 25, 32]


end = time.time()
print(f"{end - start:.5f} sec")
# 0.00002 sec

# 사용자 input
"""
import sys     

input_array = list(map(int,sys.stdin.readline().split()))
optimized_quicksort(input_array, 0, len(input_array)-1)
print(input_array)
"""
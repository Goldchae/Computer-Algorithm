import time # 시간 비교용
start = time.time()

def basic_quicksort(arr):
    """
    기본 퀵 정렬 구현으로, 최악의 경우 O(n^2) 시간 복잡도를 가질 수 있음
    이는 피벗이 반복적으로 가장 작거나 가장 큰 원소일 때 발생
    """
    # 기본 경우: 배열이 비어 있거나 하나의 원소만을 가지고 있다면 이미 정렬된 것
    if len(arr) <= 1:
        return arr
    else:
        # 피벗을 배열의 첫 번째 원소로 선택
        pivot = arr[0]
        # 배열을 피벗보다 작은 원소, 같은 원소, 큰 원소로 분할
        less = [x for x in arr[1:] if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr[1:] if x > pivot]
        # 분할된 배열에 대해 재귀적으로 퀵 정렬을 적용하고 결과를 연결
        return basic_quicksort(less) + equal + basic_quicksort(greater)

# 예제 배열
example_array = [21, 3, 12, 15, 7, 32, 4, 25, 9, 18] 
print(basic_quicksort(example_array))
## [3, 4, 7, 9, 12, 15, 18, 21, 25, 32]


end = time.time()
print(f"{end - start:.5f} sec")
# 0.00007 sec

# 사용자 input
"""
import sys     

input_array = list(map(int,sys.stdin.readline().split()))
print(basic_quicksort(input_array))
"""
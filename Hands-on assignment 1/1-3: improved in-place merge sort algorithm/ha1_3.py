
def merge(arr, l, m, r):
    """
    두 정렬된 부분 배열을 제자리에서 병합하는 함수
    arr[l:m+1] 및 arr[m+1:r+1]은 정렬된 부분 배열
    """
    i = l
    j = m + 1
    while i <= m and j <= r:
        # 첫 번째 부분 배열의 요소가 두 번째 부분 배열의 요소보다 작거나 같다면
        # 이미 올바른 위치에 있는 것
        if arr[i] <= arr[j]:
            i += 1
        else:
            # 그렇지 않다면 arr[i]와 arr[j] 사이의 요소들을 회전
            temp = arr[j]
            for k in range(j, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = temp
            # 포인터들을 조정
            i += 1
            m += 1
            j += 1


def in_place_merge_sort(arr, l, r):
    """
    추가 공간을 사용하지 않고 병합 정렬 알고리즘을 적용하는 함수
    이 함수는 재귀적으로 배열을 부분 배열로 나누고, 이를 정렬된 방식으로 병합
    """
    if l < r:
        m = l + (r - l) // 2
        in_place_merge_sort(arr, l, m)
        in_place_merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


# 예제 사용
arr_example = [12, 11, 13, 5, 6, 7]
in_place_merge_sort(arr_example, 0, len(arr_example) - 1)
print(arr_example) # [5, 6, 7, 11, 12, 13]

# 사용자 input
"""
import sys     

input_arr = list(map(int,sys.stdin.readline().split()))
in_place_merge_sort(input_arr, 0, len(input_arr)-1)
print(input_arr)
"""
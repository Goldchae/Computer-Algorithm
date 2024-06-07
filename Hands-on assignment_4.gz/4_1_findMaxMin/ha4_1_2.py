def find_max_min_type2(arr, i, j):
    # 세그먼트가 하나의 요소만 가진 경우
    if i == j:
        return arr[i], arr[i]
    
    # 세그먼트가 두 개의 요소를 가진 경우
    if j == i + 1:
        if arr[i] < arr[j]:
            return arr[i], arr[j]
        else:
            return arr[j], arr[i]
    
    # 배열을 두 개의 하위 배열로 나누기
    mid = (i + j) // 2
    min_left, max_left = find_max_min_type2(arr, i, mid)
    min_right, max_right = find_max_min_type2(arr, mid + 1, j)
    
    # 두 하위 배열의 결과를 결합
    min_val = min(min_left, min_right)
    max_val = max(max_left, max_right)
    
    return min_val, max_val

# 예제 사용
arr = [24, 75, 92, 83, 61, 48, 97, 50]
min_val, max_val = find_max_min_type2(arr, 0, len(arr) - 1)
print(f"Min: {min_val}, Max: {max_val}")

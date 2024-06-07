def find_max_min_type1(arr):
    # 첫 번째 요소로 min과 max 초기화
    min_val = arr[0]
    max_val = arr[0]
    
    # 두 번째 요소부터 배열을 순회
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]
    
    return min_val, max_val

# 예제 사용
arr = [24, 75, 92, 83, 61, 48, 97, 50]
min_val, max_val = find_max_min_type1(arr)
print(f"Min: {min_val}, Max: {max_val}")

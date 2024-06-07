# 부분집합을 찾는 백트래킹 함수
def sum_of_subsets(i, wsum, rsum, w, M, solution, solutions):
    # 현재 합이 목표 합과 일치하는 경우
    if wsum == M:
        solutions.append(solution)  # 현재 부분집합을 결과 리스트에 추가
        return True
    # 배열의 끝에 도달하지 않은 경우
    if i + 1 < len(w):
        # 다음 요소를 선택하는 경우
        if wsum + w[i + 1] <= M:
            sum_of_subsets(i + 1, wsum + w[i + 1], rsum - w[i + 1], w, M, solution + [w[i + 1]], solutions)
        # 다음 요소를 선택하지 않는 경우
        sum_of_subsets(i + 1, wsum, rsum - w[i + 1], w, M, solution, solutions)
    return False

# 확장할 수 있는지 여부를 확인하는 함수
def is_expand(i, wsum, rsum, w, M):
    # 현재까지의 합과 남은 합이 목표 합 이상인지, 다음 요소를 더해도 목표 합 이하인지 확인
    return (wsum + rsum >= M) and (wsum == M or (i + 1 < len(w) and wsum + w[i + 1] <= M))



w = [3, 34, 4, 12, 5, 2]  # 입력 배열
M = 9  # 목표 합

# 사용자 입력용!
# import sys
# w = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())

total_sum = sum(w)  # 배열의 총합 계산
solutions = []  # 가능한 부분집합을 저장할 리스트
sum_of_subsets(-1, 0, total_sum, w, M, [], solutions)  # 백트래킹 함수 호출


# 결과 출력
if solutions:
    for solution in solutions:
        print(solution)
else:
    print("No subset found")



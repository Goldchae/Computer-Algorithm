def floyd_warshall(weights):
    n = len(weights)  # 가중치 행렬의 크기, 즉 정점의 수
    # 각 정점 간의 최소 거리를 저장할 행렬 초기화
    dist = [[float('inf')] * n for _ in range(n)]
    # 최단 경로를 추적할 다음 정점 행렬 초기화
    next_node = [[None] * n for _ in range(n)]

    # 초기 거리 행렬 설정
    for i in range(n):
        for j in range(n):
            if weights[i][j] != 'INF':
                dist[i][j] = weights[i][j]
                next_node[i][j] = j
            if i == j:
                dist[i][j] = 0  # 자기 자신으로의 거리는 0

    # Floyd-Warshall 알고리즘 적용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 새로운 경로가 더 짧다면 거리 및 경로 업데이트
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node  # 결과 거리 및 경로 행렬 반환

def reconstruct_path(start, end, next_node):
    if next_node[start][end] is None:
        return []  # 경로가 없는 경우 빈 리스트 반환
    path = []
    intermediate = start
    while intermediate != end:
        path.append(intermediate)  # 경로에 정점 추가
        intermediate = next_node[intermediate][end]
    path.append(end)  # 종료 정점 추가
    return path  # 완성된 경로 반환

# 사용 예시
weights = [
    [0, 3, 'INF', 7],
    [8, 0, 2, 'INF'],
    [5, 'INF', 0, 1],
    [2, 'INF', 'INF', 0]
]

dist, next_node = floyd_warshall(weights)  # 최단 경로 계산

# 최단 경로 출력
path_v1_v3 = reconstruct_path(1, 3, next_node)
path_v0_v2 = reconstruct_path(0, 2, next_node)

print("Shortest path from v1 to v3:", path_v1_v3)
print("Shortest path from v0 to v2:", path_v0_v2)


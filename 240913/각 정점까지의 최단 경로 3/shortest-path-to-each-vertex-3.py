import sys

# 아주 큰 값을 나타내는 int_max 설정
int_max = sys.maxsize

# 정점의 수(n)와 간선의 수(m)을 입력받습니다.
n, m = map(int, input().split())

# 그래프를 인접 행렬로 표현하기 위해 2차원 리스트를 생성합니다.
graph = []
for i in range(n + 1):
    graph.append([0] * (n + 1))

# 간선 정보를 입력받고, 인접 행렬을 채웁니다.
for _ in range(1, m + 1):
    start, to, value = map(int, input().split())
    graph[start][to] = value

# 방문 여부와 최단 거리 리스트를 초기화합니다.
visited = [False] * (n + 1)
dist = [int_max] * (n + 1)

# 시작 정점의 거리는 0으로 설정합니다.
dist[1] = 0

# 다익스트라 알고리즘 O(n^2)
for i in range(1, n + 1):
    # 아직 방문하지 않은 정점 중 dist 값이 가장 작은 정점을 찾아줍니다.
    min_index = -1
    for j in range(1, n + 1):
        if not visited[j]:  # 방문하지 않은 노드만 고려
            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j

    # 최솟값에 해당하는 정점에 방문 표시를 합니다.
    if min_index == -1:
        break  # 더 이상 방문할 수 있는 노드가 없는 경우

    visited[min_index] = True  # 여기가 문제였던 부분입니다.

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며 최단 경로를 갱신합니다.
    for j in range(1, n + 1):
        if graph[min_index][j] != 0:  # 간선이 존재하는 경우에만 처리
            dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])

# 각 지점까지의 최단 거리 값을 출력합니다.
for i in range(2, n + 1):
    print(dist[i])
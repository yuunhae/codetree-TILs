import heapq

def dijkstra(n, start, graph):
    # 최단 거리 리스트를 무한대 값으로 초기화
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0  # 시작 정점의 거리는 0으로 설정
    
    # 우선순위 큐 생성 (거리, 노드)
    pq = [(0, start)]  # 시작점에서의 거리가 0이므로 (0, start)
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # 이미 처리된 노드면 건너뜁니다
        if current_dist > dist[u]:
            continue
        
        # 인접한 모든 노드에 대해 최단 경로 갱신
        for v, weight in graph[u]:
            alt = current_dist + weight  # 현재 노드까지 거리 + 간선 가중치
            if alt < dist[v]:  # 더 짧은 경로가 있다면 갱신
                dist[v] = alt
                heapq.heappush(pq, (alt, v))  # 우선순위 큐에 새로운 경로 추가
    
    return dist

# 입력 처리
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력 받기
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u에서 v로 가는 가중치 w인 간선

# 1번 정점에서 시작하는 다익스트라 알고리즘 수행
start_node = 1
distances = dijkstra(n, start_node, graph)

# 결과 출력 (2번 정점부터 n번 정점까지)
for i in range(2, n + 1):
    if distances[i] == float('inf'):
        print(-1)  # 도달할 수 없는 경우 -1 출력
    else:
        print(distances[i])
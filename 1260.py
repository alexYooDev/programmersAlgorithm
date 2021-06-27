from collections import deque

# n = 정점 개수, m = 간선 개수, v = 시작 정점 번호 
n,m,v = map(int, input().split())

# n+1개의 정점을 가진 그래프(이차원 리스트)를 생성
graph = [[0]*(n+1) for _ in range(n + 1)]

# 간선의 개수 만큼
for _ in range(m):
  # 간선이 연결하는 정점을 입력
  n1,n2 = map(int, input().split())

  # 정점을 연결
  graph[n1][n2] = graph[n2][n1] = 1

# 넓이 우선 탐색 알고리즘 함수 (매개변수는 시작 정점)
def bfs(start_node):
  
  # 방문 여부 배열 생성하여 시작 정점을 할당 
  visited = [start_node]

  #bfs를 위한 큐를 생성 (list로 pop(0)을 하면 시간복잡도가 O(N)임)
  #queue의 popleft() 사용하면 O(1) 이기 때문에 queue 사용
  queue = deque()
  #큐에 시작 정점을 넣어준다
  queue.append(start_node)
  
  #큐가 빌때 까지
  while queue:
    # v 변수에 queue를 pop한 값을 할당 (방문한 순서 대로 할당) 
    v = queue.popleft()
    # v를 출력한다
    print(v, end=' ')

    #그래프 안의 시작 노드의 길이 w 만큼
    for w in range(len(graph[start_node])):
      # 그래프[방문 정점리스트의][w]를 처음 방문하고 w이 방문 기록 리스트에 없다면
      if graph[v][w] == 1 and (w not in visited):
        #방문 기록 리스트에 w를 넣는다
        visited.append(w)
        #큐에도 넣는다.
        queue.append(w)

# 깊이 우선 탐색 알고리즘 함수 (매개변수는 시작 정점, 방문 기록 리스트)
def dfs(start_node, visited = []):
  #방문 기록 리스트에 시작 정점을 넣는다
  visited.append(start_node)
  #정점값을 출력
  print(start_node, end=' ')

  # 그래프의 시작 정점 길이 w 만큼
  for w in range(len(graph[start_node])):
    # 그래프 정점[w]를 아직 방문 하지 않았고 방문 기록 리스트에 없다면
    if graph[start_node][w] == 1 and (w not in visited):
      # dfs 함수에 매개변수로 w를 대입하여 재귀한다.
      dfs(w, visited)

bfs(v)
print()
dfs(v)

  

  
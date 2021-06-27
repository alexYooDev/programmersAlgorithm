import sys

#재귀함수 사용할 때 시간초과 방지를 위해 재귀 제한을 해제
sys.setrecursionlimit(10000)
# input을 sys.stdin.readline으로 초기화하여 실행속도 높임
input = sys.stdin.readline

# 정점의 개수와 간선의 개수 입력
n,m = map(int, input().split())
# 그래프 생성 0번 정점부터 n번 정점이 있는 그래프
graph = [[0]*(n+1) for _ in range(n+1)]
# 방문 체크 리스트 생성 
visited = [False] * (n+1)
# 연결 요소 개수 측정용
cnt = 0

# 간선의 개수 만큼
for _ in range(m):
  # 간선의 양 끝 점 u,v 입력
  u,v = map(int, input().split())
  # 그래프에서 u의 인덱스에 v를 추가
  graph[u].append(v)
  # 그래프에서 v의 인덱스에 u를 추가
  graph[v].append(u)

# 깊이 우선 탐색 알고리즘 (매개변수는 탐색 시작 정점)
def dfs(v):
  # 처음 탐색 정점을 방문 처리
  visited[v] = True
  # 시작점에 연결되어 있는 정점들 중
  for e in graph[v]:
    # 방문하지 않았다면
    if not visited[e]:
      # 그 정점을 dfs 재귀함수로 돌림
      dfs(e)

# 1부터 n까지
for j in range(1,n+1):
  # 방문되지 않았다면
  if not visited[j]:
    # 그 정점을 시작점으로 깊이 우선 탐색 재귀 실행
    dfs(j)
    # 카운트 1
    cnt +=1

# 총 카운트된 수 출력
print(cnt)

def dfs(x):
  visited[x] = True
  # 다음 탐색할 노드
  num = graph[x]
  # 다음 노드가 방문되지 않았다면
  if not visited[num]:
    # 다음노드를 dfs 재귀로 진행
    dfs(num)

# 입력한 테스트 케이스 만큼 반복
for _ in range(int(input())):
  # 순열의 크기
  n = int(input())
  # 인덱스 0은 0으로 설정, 그 다음 순열의 값을 저장 
  graph = [0] + list(map(int, input().split()))
  # 인덱스 0은 True로 처리 + 나머지 값 만큼 False => 방문처리 체크할 리스트
  visited = [True] + [False] * n
  # 카운트 변수
  count = 0

  # 인덱스 1부터 n까지 순회하며
  for i in range(1, n+1):
    # 인덱스 각각 방문이 되었는 지 확인 => 방문하지 않았다면
    if not visited[i]:
      # dfs 함수로 진행
      dfs(i)
      # count를 1씩 증가
      count += 1
  # 총 센 count를 출력 (연결되어 있는 순열 개수)
  print(count)
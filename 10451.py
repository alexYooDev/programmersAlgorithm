def dfs(x):
  visited[x] = True
  num = graph[x]
  if not visited[num]:
    dfs(num)

for _ in range(int(input())):
  n = int(input())
  graph = [0] + list(map(int, input().split()))
  visited = [True] + [False]*n
  count = 0

  for i in range(1, n+1):
    if not visited[i]:
      dfs(i)
      count += 1

  print(count)
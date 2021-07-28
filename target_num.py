answer = 0

def dfs(node, numbers, target, value):
  global answer
  length = len(numbers)
  if node == length and target == value:
    answer += 1
    return

  if node == length:
    return

  dfs(node+1, numbers, target, value+numbers[node])
  dfs(node+1, numbers, target, value-numbers[node])

def solution(numbers, target):
  global answer
  dfs(0,numbers, target, 0)
  return answer


print(solution([1,1,1,1,1], 3))
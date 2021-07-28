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

def solution(numbers, target):
  answer = dfs(numbers, target, 0)
  return answer

def dfs(numbers, target, depth):
  result = 0
  if depth == len(numbers):
    if sum(numbers) == target:
      return 1
  
    else: return 0
  
  else: 
    result += dfs(numbers, target, depth+1)
    numbers[depth] *= -1
    result += dfs(numbers, target, depth+1)
    return result

print(solution([1,1,1,1,1], 3))
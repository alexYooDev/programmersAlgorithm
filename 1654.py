k, n = map(int, input().split())

#각 소유한 랜선이 들어있는 리스트
lan = [int(input()) for i in range(k)]

# 랜선 최소, 최대 길이값
low, high = 1, max(lan)

# 1이 최대 길이값보다 작거나 같을 동안
while low <= high:
  # 중위값을 설정
  mid = (high+low)//2
  # 랜선 개수 초기화
  quantity = 0

  # 랜선 리스트의 요소들에 있어
  for i in lan:
    # 찾을 개수를 중위 값으로 나눈 값을 할당
    quantity += i//mid

  #필요한 개수 보다 클 경우
  if quantity >= n:
    #탐색 위치를 중위값 보다 큰 범위로
    low = mid+1  
  #필요한 개수 보다 작을 경우
  else:
    #탐색 위치를 최대값보다 작은 범위로
    high = mid-1
  
# 만들 수 있는 최대 랜선 길이 출력
print(high)





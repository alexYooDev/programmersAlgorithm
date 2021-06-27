n = int(input())

# dp 리스트에 n+1개의 0을 할당
dp = [0 for _ in range(n+1)]

#2부터 n+1(11 전 까지)까지 (n = 10일 경우 : 2,3,4,5,6,7,8,9,10)
for i in range(2, n+1):
  # 1을 빼고 연산 횟수를 1만큼 더함
  dp[i] = dp[i-1] + 1
  # i가 2로 나누어 떨어질 경우
  if i%2 == 0:
    # dp의 요소 값을 기존의 요소값과 요소를 2로 나눈 값 중 최소값을 구하고 회수 저장
    dp[i] = min(dp[i], dp[i//2]+1)
  # i가 3으로 나누어 떨어질 겨우
  if i%3 == 0:
    # dp의 요소 값을 기존의 요소값과 요소를 3로 나눈 값 중 최소값을 구하고 회수 저장
    dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])


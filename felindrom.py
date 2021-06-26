while True:
  n = list(input())
  rvs = []
  for i in range(len(n), 0, -1):
    rvs.append(n[i-1])
  if n == ['0']:
    break
  if n == rvs:
    print('yes')
  else:
    print('no')
num = list(map(int, input().split()))

result = []

for i in num:
  result.append(i**2)

print(sum(result)%10)
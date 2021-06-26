l, p = map(int, input().split())
news = list(map(int, input().split()))

people_num = l*p

for i in news:
  print(i-people_num, end = " ")
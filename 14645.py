n,m = map(int, input().split())

for i in range(n):
  x,y = map(int, input().split())
  m+=x
  m-=y

if x == 0:
  print('비와이')
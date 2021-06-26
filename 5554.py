time = []
min_sec = 0

for i in range(4):

  d = int(input())

  time.append(d)

min_sec = sum(time)

print(min_sec//60)
print(min_sec%60)



  
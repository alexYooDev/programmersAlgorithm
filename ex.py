n,m = map(int, input().split())

arr = []
cnt = 0

for i in range(n):
    arr.append(input())


for j in range(len(arr)):
    if j%2 == 1:
        print(arr[j][1::2])
'''  if j%2 == 1:
        if "B" in arr[j][1::2]:
            cnt+=1
        elif "W" in arr[j][::2]:
            cnt+=1
    else:
        if "W" in arr[j][1::2]:
            cnt+=1
        elif "B" in arr[j][::2]:
            cnt+=1  '''

print(cnt)



n = int(input())

#입력한 여러 수를 저장할 리스트 생성
arr = []

#n만큼 입력 반복 => 리스트에 추가
for i in range(n):
  word = input()
  arr.append(word)

# 집합자료형으로 변경 => 중복 허락하지 않기에
arr = list(set(arr))
# 글자 길이순으로 정렬 람다
arr.sort(key=lambda x: (len(x),x) )
#리스트 안 요소들을 줄바꿈으로 연결
answer = '\n'.join(arr)
print(answer)
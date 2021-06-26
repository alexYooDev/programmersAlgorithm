x,y,w,h = map(int, input().split())

# x,y에서 근접한 경계값의 차, w,h 에서 0,0안에 x,y의 경계값까지의 차
print(min([x,y,w-x,h-y]))
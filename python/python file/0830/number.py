
#ary없이 하기
for i in range(25):
    print(i+1, end=' ')
    if i % 5 == 4:
        print()
#ary없이 하기 2
for i in range(5):
    for j in range(5):
        print("%2d"%((5*i)+j+1), end=' ')
    print()

#ary로 하기
ary=[[],[],[],[],[]]
cnt=0
for i in range(5):
    for j in range(5): #반복수
        cnt=cnt+1
        ary[i].append(cnt)
        
print(ary)

for i in range(5):
    for j in range(5):
        print("%2d"%(ary[i][j]), end=' ') #i와 j는 0부터 시작한다. 즉, ary의 0번째부터 4번째까지의 리스트에서
    print()                               #0부터 4까지 뽑아오는 걸 반복한다는 뜻
ary=[[],[],[],[],[]]
cnt=26
for i in range(5):
    for j in range(5): #반복수
        cnt=cnt-1
        ary[i].append(cnt)
        
print(ary)
j=1
for i in range(5):
    print("%2d"%(ary[i][j]), end=' ') #i와 j는 0부터 시작한다. 즉, ary의 0번째부터 4번째까지 뽑아오는 걸 반복한다는 뜻
print()
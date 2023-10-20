#구구단을 세로로 내기
for i in range(1,10):
    for j in range(1,10):
        print(i*j)

#구구단을 2단을 한줄로 적은 후 3단은 다음 줄로
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')

#교수님이 푸신 방법
for i in range(1,10):
    for j in range(1,10):
        print("%2dX%2d=%2d"%(i,j,i*j))  #세로 j,i,j*i,end=''
    print()
    

#별찍기
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()

#또 다른 별 찍기 방법
for i in range(5):
    print('*'*(i+1))

a=[1,2,3,4]
result=[num*3 for num in a]
result
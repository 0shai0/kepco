#매점 판매이익 극대화 시키기
#포켓몬빵:700원, 아.아:3100원, 컵라면:1200원
#9300<i*700+j*1200+k*3100<=10000

 #cnt는 경우의 수를 확인하기 위해서 적은 것      #range에서 1로 시작하는 건 0개로 사는 이유가 없기 때문이다.
result=[]
cnt=0;total=0
for i in range(1,(10000//700)+1):
    for j in range(1,(10000//1200)+1):
        for k in range(1,(10000//3100)+1):
            changes=10000-(700*i)-(1200*j)-(3100*k)
            if (changes>=0) and (changes<700):
                total=total+1
                cnt=cnt+1
                print(f'[{cnt}] 포켓몬빵을 {i}개 구매하고', end=', ')
                print(f'컵라면을 {j}개 구매하고', end=', ')
                print(f'아.아를 {k}개 구매해서 잔돈이 {changes}원 남았습니다')
                result.append([cnt, i, j, k, changes])
print(total)

print(result)

print([List[4] for List in result])
print([List[0] for List in result])

#정렬 1번째 방법

print(sorted(result,key=lambda x:x[1]))


#정렬 2번째 방법

# 아래거는 딕셔너리 만드는 문장임

sort_result={ } #요거는 변수임. 변수를 집합 형태로 꺼내겠다는 말임
for List in result:
    if List[-1] not in sort_result:
        sort_result[List[-1]]=[ ] #여기까지는 List[-1]이 없다면 sort_result[List[-1]]는 []는 말임. 즉 이 예에선 의미 없다는 말.
    sort_result[List[-1]].append(list(List))  #append는 덧붙인다는 말임. (a,b).append(c)면 (a,b,c)로 된다는 뜻. 여기선 복붙함.
                                              #List[-1]+list(list)

print(sort_result) #이렇게 하면 딕셔너리 형태임

Key_list=list(sort_result.keys()) #조건문을 만들어서 답을 낼거기에 변수로 변경
Key_list.sort() #딕셔너리의 key값만 출력하고 그 key를 분류함

#왜 key에 []를 붙이지?
for key in Key_list:
    for List in sort_result[key]: #딕셔너리에서 key의 value 값을 뽑아내겠다임. 근데 key는 순서에 들어가지 않음. key값과 value는 별개이기에.
        print(f'[{List[0]}] 포켓몬빵을 {List[1]}개 구매하고', end=', ')
        print(f'컵라면을 {List[2]}개 구매하고', end=', ')
        print(f'아.아를 {List[3]}개 구매해서 잔돈이 {List[4]}원 남았습니다')
        
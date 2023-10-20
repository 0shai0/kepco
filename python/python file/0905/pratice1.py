glory=[['장려상',60,1,0,0],['동상',70,1,1,5],['은상',80,1,1,10],['금상',90,1,1,20]]


def prize(List,grade):
    if grade >= List[1]:
        return True #glory의 List를 준다는 것이다
    
grade=int(input("점수를 입력하세요 : "))

#함수 실행문
for idx, List in enumerate(glory[::-1]):
    if prize(List,grade):
        print(glory[::-1][idx])
        break

grade=int(input("점수를 입력하세요 : "))
for [rank, min_score,trophy,bouns,qty] in glory[::-1]:
    if grade >= min_score:
        print(f' 님, ====={rank}=====', end='')
        if qty:
            print(f'상품: 문화상품권 {qty}매')
        print()
        # for txt in [rank,qty]:
        #     if txt:
        #         print(f'{txt}', end='')
        # print()
        break
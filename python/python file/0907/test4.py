# age=int(input("나이를 입력하세요 :"))
# print("무료" if age < 8 or age > 60 else "입장료 : 5000")

v=list(range(10))
print((i if i==5 else "NO" for i in v)) # 제너레이터 형식은 하나씩 불러온다. 근데 이건 그 다음을 불러주는 for나 while이 없다.
                                        # 그러니 하나로 묶어서 읽으라고 하기 위해 리스트로 묶는다.


# list_a=list(range(10))
# list_b = [i if i > 3 else "same" if i == 2 else "under" for i in list_a ]
# print(list_b)
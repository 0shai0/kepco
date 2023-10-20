coffe=10
money=1000
while True:
    int(input("100원을 넣으세요 : "))
    print("커피를 받으세요")
    money=money-100
    coffe=coffe-1
    print("거스름돈 %d원입니다"%money)
    print("커피가 %d개 남았습니다"%coffe)
    if coffe==0:
        print("커피가 다 떨어졌습니다")
        
        break
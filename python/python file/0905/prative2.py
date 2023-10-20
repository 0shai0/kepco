name=['may','kein','kain','kali','mari','don']
yearning=[5,10,1,11,1,55]
miss=[('may',5),('kein',10),('kain',1),('kali',11),('mari',1),('don',55)]
photo=(input("사진에 넣을 인물들을 name에서 골라 적어주세요 ex) may,kein : "))

# 해결해야할 문제
# 포토에서 인물들을 치면 yearning에 있는 숫자들을 더해야한다.
# 여기서 1을 찾을 때 3번 째 있는 것에서만 찾음. find 같이 - 이거 해결하기

def score(name,yearning):
    for i in range(6):
        if miss[i][0] == 'may':
            print(f'{miss[i][1]}')
            if: miss[i][0] == 'kein':
                print(f'{miss[i][1]}')
                if  miss[i][0] == 'kain':
                    print(f'{miss[i][1]}')
                    if miss[i][0] == 'kali':
                        print(f'{miss[i][1]}')
                        if miss[i][0] == 'mari':
                            print(f'{miss[i][1]}')
                            if miss[i][0] == 'don':
                                print(f'{miss[i][1]}')

score(name,yearning)
# while True:
#     Q=input("이름을 더 적겠습니까? Y/N : ")
#     q=['Y']
#     if Q == q:
#         score(name,yearning)
#     break












        
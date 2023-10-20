#com=[a,b,c], user[a,b,c] 스트라이크 게임 만들기
#결과로 0S, 0B 형태로 만들기, 만일 3S라면 종료되게 만들기
#둘 다 중복제거
#random을 써라
import random
numberlist=[1,2,3,4,5,6,7,8,9]
answer=[]

class baseball:
    def __init__(self):
        self.COM=[]
        self.USER=[]
        self.cnt=0

    def makenumber(self): #랜덤 숫자를 고정시키기 위해 따로 만들고 아래에 while문을 만듬
        self.COM=random.sample(numberlist,3)

    def getnumber(self):
        answer=[]
        while len(answer)!=3:
            answer=list(map(int,input("1~9까지의 숫자에서 3개를 골라 적어주세요. ex) 1,2,3 : ").split(",")))
            if answer[0] == answer[1] or answer[0] == answer[2] or answer[1] == answer[2]:
                print("숫자를 중복되지 않게 작성해주세요")
                break
            self.USER=answer
            self.cnt += 1
            #self.cnt 값을 어떻게 리턴시키지?
    
    def match(self): 
        if self.USER[0] or self.USER[1] or self.USER[2] in self.COM:
            if self.COM[0] in self.USER:
                if self.COM[0] == self.USER[0]:
                    if self.COM[1] in self.USER:
                        if self.COM[1] == self.USER[1]:
                            if self.COM[2] in self.USER:
                                if self.COM[2] == self.USER[2]:
                                    print(f"[{self.cnt}] 3 strike입니다 {self.COM}")
                                else:
                                    print(f"[{self.cnt}] 2 strike, 1 ball입니다 {self.COM}")
                            else:
                                print(f"[{self.cnt}] 2 strike, 0 ball입니다 {self.COM}")
                        else:
                            print(f"[{self.cnt}] 1 strike, 1 ball입니다 {self.COM}")
                    else:
                        if self.COM[2] in self.USER:
                            if self.COM[2] == self.USER[2]:                                
                                if self.COM[1] in self.USER[1]:
                                    if self.COM[1] == self.USER[1]:
                                        print(f"[{self.cnt}] 3 strike입니다 {self.COM}")
                                    else:
                                        print(f"[{self.cnt}] 2 strike, 1 ball입니다 {self.COM}")
                                else:
                                    print(f"[{self.cnt}] 2 strike, 0 ball입니다 {self.COM}")
                            else:
                                print(f"[{self.cnt}] 1 strike, 1 ball입니다 {self.COM}")
                        else:
                            print(f"[{self.cnt}] 1 strike, 0 ball입니다 {self.COM}")
                else:


                    print(f"[{self.cnt}] 0 strike, 1 ball입니다 {self.COM}")
            else:
                if self.COM[1] in self.USER:
                    if self.COM[1] == self.USER[1]:
                        if self.COM[0] in self.USER:
                            if self.COM[0] == self.USER[0]:
                                if self.COM[2] in self.USER:
                                    if self.COM[2] == self.USER[2]:
                                        print(f"[{self.cnt}] 3 strike입니다 {self.COM}")
                                    else:
                                        print(f"[{self.cnt}] 2 strike, 1 ball입니다 {self.COM}")
                                else:
                                    print(f"[{self.cnt}] 2 strike, 0 ball입니다 {self.COM}")
                            else:
                                print(f"[{self.cnt}] 1 strike, 1 ball입니다 {self.COM}")
                        else:
                            if self.COM[2] in self.USER:
                                if self.COM[2] == self.USER[2]:
                                    if self.COM[0] in self.USER[0]:
                                        if self.COM[0] == self.USER[0]:
                                            print(f"[{self.cnt}] 3 strike입니다 {self.COM}")
                                        else:
                                            print(f"[{self.cnt}] 2 strike, 1 ball입니다 {self.COM}")
                                    else:
                                        print(f"[{self.cnt}] 2 strike, 0 ball입니다 {self.COM}")
                                else:
                                    print(f"[{self.cnt}] 1 strike, 1 ball입니다 {self.COM}")
                            else:
                                print(f"[{self.cnt}] 1 strike, 0 ball입니다 {self.COM}")
                    else:
                        print(f"[{self.cnt}] 0 strike, 1 ball입니다 {self.COM}")
                else:
                    if self.COM[2] in self.USER:
                        if self.COM[2] == self.USER[2]:
                            if self.COM[0] in self.USER:
                                if self.COM[0] == self.USER[0]:
                                    if self.COM[1] in self.USER:
                                        if self.COM[1] == self.USER[1]:
                                            print(f"[{self.cnt}] 3 strike입니다 {self.COM}")
                                        else:
                                            print(f"[{self.cnt}] 2 strike, 1 ball입니다 {self.COM}")
                                    else:
                                        print(f"[{self.cnt}] 2 strike, 0 ball입니다 {self.COM}")
                                else:
                                    print(f"[{self.cnt}] 1 strike, 1 ball입니다 {self.COM}")
                            else:
                                if self.COM[1] in self.USER:
                                    if self.COM[1] == self.USER[1]:
                                        if self.COM[0] in self.USER[0]:
                                            if self.COM[0] == self.USER[0]:
                                                print(f"[{self.cnt}] 3 strike입니다 {self.COM}")
                                            else:
                                                print(f"[{self.cnt}] 2 strike, 1 ball입니다 {self.COM}")
                                        else:
                                            print(f"[{self.cnt}] 1 strike, 1 ball입니다 {self.COM}")
                                    else:
                                        print(f"[{self.cnt}] 2 strike, 0 ball입니다 {self.COM}")
                                else:
                                    print(f"[{self.cnt}] 1 stike, 0 ball입니다 {self.COM}")
                        
                        else:
                            print(f"[{self.cnt}] 0 strike, 1 ball입니다 {self.COM}")
        else:
            print(f"[{self.cnt}] 0 strike, 0 ball입니다. {self.COM}")
        
    
run=baseball()
run.makenumber()
while True:
    run.getnumber()
    run.match()
    if run.cnt==10 or run.COM[0]==run.USER[0] and run.COM[1]==run.USER[1] and run.COM[2]==run.USER[2]:
        print("축하합니다. 이기셨습니다.")
        break

#숫자 입력할 때 중복되지 않게, print 공백이 되지 않게, 3 strike면 종료, 10번 하면 끝
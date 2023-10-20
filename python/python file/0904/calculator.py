#계산기를 만들어보자!!
#할 일
# 전에 쳤던 숫자 기억시키기 (return, while)


class calculator:
    def __init__(self):
        self.number=0
        self.result=0

    def plus(self):
        self.number=int(input("정수인 숫자를 넣어주세요. : "))
        self.result+=self.number
        print(self.result)
        return self.result
    
    def minus(self):
        self.number=int(input("정수인 숫자를 넣어주세요. : "))
        self.result-=self.number
        print(self.result)
        return self.result
       

    def multiplication(self):
        self.number=int(input("정수인 숫자를 넣어주세요. : "))
        if self.result == 0 or self.number==0:
            print("0을 곱할 수는 없습니다")
        else:
            self.result*=self.number
            print(self.result)
            return self.result
       
    
#소수점이 나오는 경우가 아니면 .0이 안나오 게 할 순 없나?

    def divide(self):
        self.number=int(input("정수인 숫자를 넣어주세요. : "))
        if self.result == 0 or self.number==0:
            print("0을 나눌 수는 없습니다")
        else:
            self.result//=self.number
            print(self.result)
            return self.result
        



run=calculator()


while True: #input 넣기
    a=input("어떤 걸 하실 건가요? 덧셈/뺄셈/곱셈/나눗셈/그만할게 : ")
    b=["덧셈","뺄셈","곱셈","나눗셈","그만할게"]
    if a == b[0]:
        run.plus()
    elif a == b[1]:
        run.minus()
    elif a == b[2]:
        run.multiplication()
    elif a == b[3]:
        run.divide()
    elif a == b[4]:
        print("계산기를 종료합니다")
        break
    else:
        print("다시 작성해주세요")

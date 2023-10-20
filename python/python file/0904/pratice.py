while True:
    a=int(input("첫 번째 정수인 숫자를 입력하세요 : "))
    b=int(input("두번째 정수인 숫자를 입력하세요 : "))
    c=int(input("세번째 정수인 숫자를 입력하세요 : "))
    break

sum=a+b+c
print(sum,sum/3)


cm=int(input("cm를 입력하세요 : "))
m=cm//100
cm=cm%100
print(f"{m}m, {cm}cm")
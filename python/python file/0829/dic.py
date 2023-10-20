dic=dict()
for key in 'abcdefghijklmnopqrstuvwxyz':
    if key not in dic:
        dic[key]=0

name = input("이름을 적어주세요 : ")
for key in name:
    dic[key]=dic[key]+1 #key의 value를 찾아서 +1한다는 뜻임
    print(dic)
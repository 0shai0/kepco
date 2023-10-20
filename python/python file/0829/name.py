
#알파벳 개수 찾기 (내가 한 것)
while True:
    name=input("이름을 입력하세요 : ")
    print(name.count('a'))
    print(name.count('b'))
    print(name.count('c'))
    print(name.count('d'))
    print(name.count('e'))
    print(name.count('f'))
    print(name.count('g'))
    print(name.count('h'))
    print(name.count('i'))
    print(name.count('j'))
    print(name.count('k'))
    print(name.count('l'))
    print(name.count('m'))
    print(name.count('n'))
    print(name.count('o'))
    print(name.count('p'))
    print(name.count('q'))
    print(name.count('r'))
    print(name.count('s'))
    print(name.count('t'))
    print(name.count('u'))
    print(name.count('v'))
    print(name.count('w'))
    print(name.count('x'))
    print(name.count('y'))
    print(name.count('z'))
    break

#교수님이 한 것

alphabet = 'abcdefghijklmnopqrstuvwxyz'
name=input('이름을 입력하세요 : ')
for e in alphabet: #for문은 하나씩 가져오는 거임
    print(e,':',name.count(e)) #name.count(e)는 알파벳에서 가져온 글자 하나가 이름에 몇 개 있는지 세는 것



dic=dict()
for key in 'abcdefghijklmnopqrstuvwxyz':
    if key not in dic:
        dic[key]=0

name = input("이름을 적어주세요 : ")
for key in name:
    dic[key]=dic[key]+1
    print(dic)


# 주사위는 4개
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


dice=['a','b','c','d']
result=[]
import random 
for i in range(4):
    for result in range(1,7):
        final=[[dice[0],result[0]],[dice[1],result[1]],[dice[2],result[2]],[dice[3],result[3]]]
        print(final)


# if 4개 주사위 number가 같을 때 1111 × p
# elif: 3개의 주사위 숫자가 일치할 경우 q=i - (10 × p + q)2
# elif: 여기 p,q는 두 개 주사위가 일치했을 때 경우 (p + q) × |p - q|
# elif: 두 개 주사위에서 같은 숫자 p, 그리고 그 숫자와 각각 다른 q,r이면 q × r
# elif: 모두 다르면 가장 적은 숫자를 점수로 얻음


#해설진이 이름을 부르면 이름의 순서, 등수가 바뀜
#선수 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players 매개변수
#해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수
#경주가 끝나면 1등부터 등수 배열을 담기


#해결법 idx를 찾고 idx-1<>idx의 선수 이름을 상호 변경하기

players=["mumu","soe","poe","kai","mine"]
callings=["kai","kai","mine","mine"]
# result=["mumu","kai","mine","soe","poe"]
def solution(players, callings):
    for player in callings:
        idx=players.index(player) #이게 뭐지..?
        players[idx]=players[idx-1]
        players[idx-1]=players[idx] #위에 것만 하면 이름이 같아지기에 순서만 바꾼다고 한 것이다. 순서를 바꾼 후 이름 선언을 한 것이다.
        #players[idx],players[idx-1]=players[idx-1],players[idx] 이렇게 한 줄로도 가능

        # 2번째 방법은
        # players.pop(idx)
        # players.insert(idx-1,players)
        print(idx)
        print(players)
    return players

solution(players,callings) #클래스가 아니라 객채가 없기에 함수 자체를 불러준다
array=[149, 180, 192, 170]
height=int(input("당신의 키를 입력해주세요"))

def solution(array, height):
    for i in range(149,200):
        Array=array.index(i)
        if height < array[Array]:
            print(array[Array].count())

solution(array, height)
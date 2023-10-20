def myMax(*tuple):
    max=0
    for i in tuple:
        if i > max:
            max=i
    print(max)

myMax(1,2,3,4,5000)
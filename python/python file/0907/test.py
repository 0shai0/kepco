def my():
    for i in range(1,1000):
        result=i*i
        yield result

gen=my()
print(next(gen))
print(next(gen))
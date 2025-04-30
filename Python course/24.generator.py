def generator(number):
    i=0
    while i < number:
        print(i)
        yield i
        i+=1

for n in generator(1000):
    print(n)
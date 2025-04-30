def printName():
    global name
    name=name+"!!!"
    print(name)

name=input("Enter your name:")
printName()

print("-"*30)
print("-"*30)
print("-"*30)

def printPerson(**person): #dictionariy
    print(person["name"],end=" ")

printPerson(name="jef" ,age=12)
print("-"*30)
print("-"*30)
print("-"*30)
def printDate(*date):
    print(date)

printDate(1,30,"40")
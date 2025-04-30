EndOfProgram=False

while not EndOfProgram:
    Name=input("name :")
    if len(Name)<2:
        EndOfProgram=True
        continue
    else:
        Age=int(input("Age :"))
        if Age>25:
            Childeren=int(input("childeren"))
            if Childeren>0:
                for n in range(Childeren):
                   child_name =input("name child: ")
        else:
            mother_name=input("name mother: ")
print("Au revoir")


landen=["Argentinie",
        "Belgie",
        "Brazilie",
        "Canade",
        "Denemarke",
        "Estonie",
        "Zambia"]

list=[0,1,2,3,4,5,6,7,8,9]
comprehension =[e*2 for e in list ]
print(comprehension)
print("-"*25)
matrix=[[1,1],[2,1],[4,2],[5,3],[2,2]]
x=matrix[1][0]


print([d+":" for d in landen if len(d)<7])
nieuwe_landen=landen.copy()
nieuwe_landen.append("nieuwe_zeeland")
print("-"*25)
print("landen:",landen)
print("-"*25)
print("nieuwe landen:",nieuwe_landen)
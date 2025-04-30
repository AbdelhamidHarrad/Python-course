landen =[
    "Belgie",
    "Spanje",
    "Frankrijk",
    ]
landen.append("jef") #toevoegen
landen.insert(0,"Italie")#toevoegen in een bepaalde index nummer
landen.remove("jef")#verwijderen uit list
europa=landen.pop(1)
landen.sort(reverse=True)


print("De eerste land in de lijst:",landen[0])
print("lijst:",landen)
print("lengte van de lijst:",len(landen)) #lengte list

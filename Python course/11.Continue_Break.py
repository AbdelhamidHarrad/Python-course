# stopt wnr je 0 invult
while input("number") != "0":
     print("ok")

totaal = 0
for x in range(10):
    totaal+=x
    if x>5:

        continue
    # Break zorgt dat de loop vroegteidig wordt verbroken
    #continue zorgt dat de volgende regels niet worden uitgevoerd maar terug verder naar de begin van de loop gaat 
    
    print(".",x)
    
print(totaal)
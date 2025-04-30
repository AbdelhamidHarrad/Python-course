talen={"taal1":"python","taal2":".Net"}
talen["taal3"]="html"
print(talen["taal1"])
print(talen)

taal4= talen.get("taal4","bestaat niet")
print(taal4)

if "taal3" in talen:
    print("beschikbaar")
else:
    print("niet beschikbaar")
      

talen["taal2"]="css"
print(talen["taal2"])
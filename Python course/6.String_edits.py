#concatenate strings
name ="Abdelhamid's pc"
message=name+" is a good pc"
print(message)

#length of string
length=len(message)
print("yor message contains "+ str(length) + " characters")
#of print("yor message contains ", length , " characters")

print("-"*40)

print(message.upper()) #upercase method
print(message.title()) #title method
new_message=message.replace("Abdelhamid's pc", "Abdelhamid's laptop") #replace method
print(new_message) #replace method
count=new_message.count("Abdelhamid's laptop") #count method
print(count) #count method
print(new_message[5])
# ctrl+/ comment/uncomment
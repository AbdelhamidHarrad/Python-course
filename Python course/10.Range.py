price_Total=0
for number in range(1,11):
   price =input("the prise of item "+str(number)+" :")
   price_Total +=int(price)
    
print("the total price of the card is "+str(price_Total))
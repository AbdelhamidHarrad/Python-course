# try:
#    number=int(input("Enter a number:"))
#    try:
#     result=10/number
#    except ZeroDivisionError:
#     print("sorry we can't divide by zero")
#    else:
#     print("the result is",result)
      
# except ValueError:
#    print("didn't work ")
# except KeyboardInterrupt:
#    print("you pressed ctrl+c")
# else:
#    print("your number is", number)
# finally:
#    print("au revoir")

def calculate_discount(price, discount_rate):
  if discount_rate < 0:
    raise ValueError("discount rate should be <0")
  else:
    dis = price - (price * discount_rate)
    print(dis)

calculate_discount(10,0)

def functie():
    print("ik ben een funtie")
    return "ik ben weg"

message=functie()
print(message)
  

def opervlakte_vierkant():
   rect_length = 10
   rect_width = 5
   rect_area = rect_length * rect_width
   print("Area of the Rectangle", rect_area)

def opervlakte_cirkel():    
    circle_radius = 12
    pi = 3.14159

    circle_area = pi * circle_radius ** 2
    print("Area of the Circle", circle_area)

opervlakte_vierkant()
opervlakte_cirkel()
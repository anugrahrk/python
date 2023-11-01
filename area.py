area_s=lambda a:a*a
area_react=lambda l,b:l*b
area_traingle=lambda b1,h:0.5*b1*h
a=int(input("Enter the side of the square"))
print("Area of square",area_s(a))
l=int(input("Enter the lenght of rectangle"))
b=int(input("Enter the breadth of rectangle"))
print("Area of rectangle",area_react(l,b))
b1=int(input("Ener the base of triangle"))
h=int(input("Enter the height of traingle"))
print("Area o traingle",area_traingle(b1,h))


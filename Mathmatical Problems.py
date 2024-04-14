#Write downa  program to find the area and Perimeter of a Square
'''
L = int(input("Enter the side of the Square (in cm.) : "))
Area = L ** 2
Perimeter = 4 * L
print("Area of Square is: ",Area,"sq. cm")
print("Perimeter of Square is: ",Perimeter,"cm")'''


#Find the area and circumference of a circle
''' 
Radius = int(input("Enter the radius value of circle (in cm.) : "))
Py_Value = 3.142
Area = Py_Value * Radius ** 2
Circumference = 2 * Py_Value *  Radius
print("Area of Circle is: ",Area,"sq. cm")
print("Circumference of Circle is: ",Circumference,"cm") '''

#Find the area and perimeter of a Cuboid.
'''
Length = int(input("Enter the length of Cuboid (in cm.) : "))
Breadth = int(input("Enter the width of Cuboid (in cm.) : "))
Height = int(input("Enter the hight of Cuboid (in cm.) : "))
Area = 2*(Height*Length + Breadth*Length + Breadth*Height)
Perimeter = 4*(Length + Breadth + Height)
print("Area of Cuboid is: ",Area,"sq. cm")
print("Perimeter of cuboid is: ", Perimeter, "cm")'''

#Find the area and perimeter of a Cube.
'''
Length = int(input("Enter the side of Cube (in cm.) : "))
Area = 6 * (Length ** 2)
Perimeter = 12 * Length
print("Area of Cuboid is: ",Area,"sq. cm")
print("Perimeter of cuboid is: ", Perimeter, "cm")'''

#Find the Total surface area of a Cylinder.
'''
Height = int(input("Enter the Height of Cylinder (in cm.) : "))
Radius = int(input("Enter the Radius of Cylinder (in cm.) : "))
py_Value = 3.142
Area = 2*py_Value*Radius*(Height + Radius)
print("The Surface Area of a cylinder is: ",Area,"sq. cm")'''

#Find the Total Surface Area of a Cone.
'''
Radius = int(input("Enter the Radius of Cone (in cm.) : "))
Slant = int(input("Enter the Slant Height of Cone (in cm.) : "))
py_Value = 3.142
Area = py_Value * Radius *(Radius + Slant)
print("The Surface Area of a Cone is: ",Area,"sq. cm")'''

#Find the Simple Interest and Amount.
'''
principal = int(input("Enter the Principal amount: "))
years = int(input("Enter the number of years: "))
Rate = float(input("Enter the rate of Interest: "))
Simple_Interest = (principal * years * Rate)/100
print("Simple Interest = ",Simple_Interest)
print("Amount = ", Simple_Interest + principal)'''

#Find the Compound Interest and Amount.
'''
principal = int(input("Enter the Principal amount: "))
years = int(input("Enter the number of years: "))
Rate = float(input("Enter the rate of Interest: "))
Amount = principal * ((1 + Rate /100 ) ** years)
print(" The Compund Interest = ", Amount - principal)
print ("Amount = ",Amount)'''

#Convert a Celsius value into Fahrenheit value
'''
Celsius = float(input("Enter the Celcius Value : "))
Fahrenheit = Celsius * 1.8 + 32
print("Fahrenheit = ",round(Fahrenheit,2))'''
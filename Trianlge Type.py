#Determine the type of a Triangle based on the lengths of it's sides
first_side = int(input("Enter first side : "))
second_side = int(input("Enter second side : "))
third_side = int(input("Enter third side : "))

if first_side == second_side == third_side:
    print('Equilateral Triangle')
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')
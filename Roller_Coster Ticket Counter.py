#Roller Coster Ticket Counter Program
print('Welcome to the Game of Roller_Coster')

height = int(input('Enter the height in cm. : '))
age = int(input('Enter the age : '))

if height >= 100:
    if  age <= 12:
        print('You can ride')
        print('Ticket Price will be Rs. 50')
    elif age < 18:
        print('You can ride')
        print('Ticket Price will be Rs. 70')
    elif age < 60:
        print('You can ride')
        print('Ticket Price will be Rs. 100')
    else:
        print("You can't ride")
        print("You're not eligible")
else:
    print("You can't ride")
    print("You're not eligible")
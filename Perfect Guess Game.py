#Perfect Guess Game
import random
name = input('Write your Name : ')
print('***Welcome to the Game of Perfect Guess',name,'***')

a = random.randint(1,100)
x = 0
Input = int(input('Write down a number between 1 to 100 : '))
while True:
    x+=1
    if Input == a:
        print('Perfect Match')
        break
    else:
        if Input > a:
            print('A Smaller Number')
        else:
            print('A Bigger Number')
        Input = int(input('Try again: '))
print(f'You guessed the correct number in {x} gusses')

'''#find if year is leap year or not
Year = int(input('Please enter the year : '))

if (Year % 4) != 0:
        print("Not a Leap Year")
elif (Year % 100) == 0 and (Year % 400) != 0:
        print('Not a Leap Year')
else:
        print('Leap Year')
'''

#Or there is another way to validate leap year
Year = int(input('Please enter the year : '))

if (Year % 4) == 0:
        if Year % 100 == 0:
                if Year % 400 == 0:
                        print('Leap Year')
                else:
                        print('Not a leap year')
        else:
                print('Leap Year')
else:
        print('Not a leap year')


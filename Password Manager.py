#Password Manager Program
print('Password Manager Menu:\n','1. Add New Password\n','2. View all Passwords\n', '3. Search for a password\n', '4. Update a Password\n', '5. Exit')

import base64
b = []
while True:
    main = int(input('Enter your choice (1-5) : '))

    if main == 1:
        b.append({'Website ': input('Website : '),'username ': input('username : '),'password ': input('password : ')})
        print('Password added successfully!')

    elif main == 2:
        for i in b:
            for y,z in i.items():
                print(y,z)
            print('----------------')
    elif main == 3:
        website = input('Enter Website Name :')
        for i in b:
            if website in i.values():
                for x,y in i.items():
                    print(x,y)
    elif main == 4:
        website = input('Enter Website Name :')
        for i in b:
            if website in i.values():
                i.update({'Website ': input('Website : '),'username ': input('username : '),'password ': input('password : ')})
                print('Password added successfully!')
    elif main == 5:
        print('Thank you for using the Password Manager. Goodbye!')
        break
    else:
        print('Please Enter Between 1-5 Only!')
        

#Pizza Shop Billing Counter Calculator
print("             ***Welcome to Saifi's Secret Ovens***")
print('             =====================================')
'''
Small = 150
Medium = 200
Large = 250
'''

Pizza = input('What size of pizza do you want? Small(S), Mediun(M) or Large(L) : ').upper()
Cheese = input('Do you want extra cheese (Rs. 30) ? Y or N :').upper()
Tomato = input('Do you want extra tomato (Rs. 30) ? Y or N :').upper()
Capsicum = input('Do you want extra capsicum (Rs. 30) ? Y or N :').upper()
Corn = input('Do you want extra corn (Rs. 20) ? Y or N :').upper()
Onion = input('Do you want extra onion (Rs. 20) ? Y or N :').upper()

Pizza_Price = 150 if Pizza == 'S' else 200 if Pizza == 'M' else 250

Total = (30 if Cheese == 'Y' else 0) + (30 if Tomato == 'Y' else 0) + (30 if Capsicum == 'Y' else 0) + (20 if Corn == 'Y' else 0) + (20 if Onion == 'Y' else 0) + Pizza_Price

print('Your Bill will be : Rs.',Total)
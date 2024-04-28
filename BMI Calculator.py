#Body Mass Index Calculator
height = int(input('Enter the height in cm. : '))
weight = int(input('Enter the weight in kg. : '))

BMI = round(weight / (height/100) ** 2,2)

if BMI <= 18.4:
    print('You are underweight. BMI :',BMI)
elif BMI < 25:
    print('You are Normal. BMI :',BMI)
elif BMI < 40:
    print('You are Overweight. BMI :',BMI)
else:
    print('You are Obese. BMI :',BMI)
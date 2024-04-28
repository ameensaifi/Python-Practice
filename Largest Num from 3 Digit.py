#find the larget of three numbers
num_1 = int(input("First Num : "))
num_2 = int(input("Second Num : "))
num_3 = int(input("Third Num : "))

if num_1 > num_2:
    if num_1 > num_3:
        print("Largest Num is",num_1)
    elif num_3 > num_2:
        print("Largest Num is",num_3)
elif num_2 > num_1:
    if  num_2 > num_3:
        print("Largest Num is", num_2)
    elif num_3 > num_2:
        print("Largest Num is", num_3)
else:
    print("Largest Num is", num_3)

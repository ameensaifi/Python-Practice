#Welcome to the tip calculator
Bill = int(input("What was the total bill ? : "))
Tip = int(input("What % would you like to give the tip ? : "))
People = int(input("How many people to split the bill ? : "))
GST = 18
Total_Bill = Bill + (Bill*GST/100)
Tip_Amt = Total_Bill * Tip/100 
Spent = Total_Bill + Tip_Amt
BillPerPerson = Spent // People
print("Per Person Split is",BillPerPerson)
#UPPCL Electricity Units Calculation
consumer_id = input('Consumer ID : ')
consumer_name = input('Consumer Name : ')
last = int(input('Old Reading Units : '))
current = int(input('Current Reading Units : '))

fixed = 250
tax = 11.5
consumed = current-last
unit_charge_below_100 = 3.25
unit_charge_post_100 = 4.75
usage = consumed*(unit_charge_below_100 if consumed <= 100 else unit_charge_post_100)
tax_amount = (fixed+usage)*tax/100
final_amount = usage+fixed+tax_amount

print('\t\t\t\t**********************************************')
print('\t\t\t\t\tUTTAR PRADESH POWER CORPORATION LIMITED')
print('\t\t\t\t\t\tBill for Supply of Electricity')
print('Circle : UP West\t\tCircle Code : 105\t\tTollFreeNo. :18001800440')
print('\t\t\t\t----------------------------------------------')
print('\tConsumer ID :\t\t\t\t\t\t\t',consumer_id)
print('\tConsumer Name :\t\t\t\t\t\t\t',consumer_name)
print('\tOld Meter Reading :\t\t\t\t\t\t',last)
print('\tCurrent Meter Reading :\t\t\t\t\t',current)
print('\tTotal Units Consumed :\t\t\t\t\t', consumed)
print('\tFixed Rental Line Maintenance Charge :\t',fixed)
print('\tTotal Usage :\t\t\t\t\t\t\t',usage)
print('\tTotal Tax (11.5%) :\t\t\t\t\t\t',tax_amount)
print('\t\t\t\t----------------------------------------------')
print('\tTotal Bill Amount Payable :\t\t\t\t', round(final_amount,2))
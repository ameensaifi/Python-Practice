#Write a program to take input of obtained marks (out of 100) in various subjects (at least 5 subjects ) of a student and calculate its Grand total, total percentage and average.

English = int(input("Marks in English : "))
Hindi = int(input("Marks in Hindi : "))
Science = int(input("Marks in Science : "))
Math = int(input("Marks in Math : "))
SST = int(input("Marks in SST : "))
GT = (English + Hindi + Science + Math + SST)
Max = 100 * 5
Average = (English + Hindi + Science + Math + SST)/5
Perc = GT / Max *100
print("The Grand Total is", GT)
print("The Percentage of marks is", str(round(Perc,2))+"%")
print("The Average of Marks is", Average)

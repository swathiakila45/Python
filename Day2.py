#Day2 Challenge 

#tip Calculator 

print("Welcome to tip calculator!")
bill=float(input("Enter the bill amount $ "))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent=tip/100
total_tip_amount= bill*tip_as_percent
total_bill =bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)

#the above round function gives only one decimal number in certain cases eg 132.60=> 132.6 neglecting the zero
# to make sure we always get two decimal places 

final_amount="{:.2f}".format(final_amount)
print(f"Each person should pay: ${final_amount}")
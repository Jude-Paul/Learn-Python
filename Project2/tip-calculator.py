print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percent = input("What percentage tip would you like to give? 10, 12, or 15 ?")
people = input("How many people to split the bill? ") 

bill = float(bill)
percent = int(percent)
people = int(people)

tip = percent / 100
tip = bill * tip
tip = bill + tip
tip = float(tip / people)

format_tip = round(tip,2)
format_tip = "{:.2f}".format(tip)
print (f"Each person should pay: ${format_tip}")

"""
Build a Bill Calculator with Tip and split options
"""

print("Welcome to the Tip Calculator!")

bill = float(input("What's the total bill?"))

tip = int(input("How much tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people to split the bill with?"))

bill_per_person = round( (bill + ((bill * tip) /100)) / people , 2)

print(f"Each person should pay: ${bill_per_person}")
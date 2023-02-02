# Tip Calculator Second

print("Welcome to the tip calculator and price divider")
total = float(input("To Begin, Please provide the total bill: $"))

tip = (int(input("How much tip would you like to give? (This is a Percentage) ")))

people = int(input("How many people are splitting the bill? "))

each_person = round(total * (1 + (tip/100)) / people, 2)

print(f'Each person should pay: ${each_person}')
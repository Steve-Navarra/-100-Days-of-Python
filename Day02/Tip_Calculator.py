print("Welcome to the tip calculator!")
bill = float(input("What was the total for the bill? "))
tip = int(input("How much would you like to tip? 10, 12, 15? "))
split = int(input("How many people are splitting the bill? "))
bill_with_tip = tip / 100 * bill + bill 
bill_per_person = bill_with_tip / split
total = round(bill_per_person,2)
print(f"each person should pay: ${total}")

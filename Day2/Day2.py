print("Hello"[-1]) 

print(type(len("123"))) #int

print(70 + float("100.5")) #170.5

print(4 ** 2) #16
print(4 ** 3) #64

print(round(8 / 3, 2)) #2.67

print(int("5") / int(2.7)) #2.5
print(int("5") // int(2.7)) #2

score = 100
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")

print("Welcome to the tip calculator!")

# Get the bill amount (using float to handle decimal numbers)
bill = float(input("What was the total bill? $"))

# Get the tip percentage (offering common tip options)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Get number of people to split the bill
people = int(input("How many people to split the bill? "))

# Calculate the total with tip
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# Calculate amount per person and round to 2 decimal places
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(final_amount)  # Ensures two decimal places are shown

print(f"Each person should pay: ${final_amount}")


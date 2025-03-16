def InputTest():
    print("Hello"[-1]) 

    print(type(len("123"))) #int

    print(70 + float("100.5")) #170.5

    print(4 ** 2) #16
    print(4 ** 3) #64

    print(round(8 / 3, 2)) #2.67

    print(int("5") / int(2.7)) #2.5
    print(int("5") // int(2.7)) #2

InputTest()

score = 100
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
def calculate_bill_per_person(bill, tip, people):
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    final_amount = "{:.2f}".format(final_amount) 
    return final_amount   
def calculate_bill():
    final_amount = calculate_bill_per_person(bill, tip, people)
    print(f"Each person should pay: ${final_amount}") 
calculate_bill()



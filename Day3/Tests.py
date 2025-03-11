# BMI Calculator with Interpretations

# Get height and weight inputs from the user
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = round(weight / (height ** 2))

# Interpret BMI and print the result
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
else:
    print(f"Your BMI is {bmi}, you are overweight.")

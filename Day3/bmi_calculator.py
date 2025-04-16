import pytest

def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI based on weight and height."""
    if height <= 0:
        raise ValueError("Height must be positive.")
    if weight <= 0:
        raise ValueError("Weight must be positive.")

    return round(weight / (height ** 2))

def interpret_bmi(bmi: float) -> str:
    """Interpret BMI and return a string with the interpretation."""
    if bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif bmi < 25:
        return f"Your BMI is {bmi}, you have a normal weight."
    
    return f"Your BMI is {bmi}, you are overweight."
    

def main():
    try:
        # Get height and weight inputs from the user
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
 
        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Interpret BMI and print the result
        print(interpret_bmi(bmi))

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Height cannot be zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This makes the script runnable directrly but allows importing functions
if  __name__ == "__main__":
    main()


# BMI Calculator with Interpretations

# # Get height and weight inputs from the user
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kilograms: "))

# # Calculate BMI
# bmi = round(weight / (height ** 2))

# # Interpret BMI and print the result
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# else:
#     print(f"Your BMI is {bmi}, you are overweight.")

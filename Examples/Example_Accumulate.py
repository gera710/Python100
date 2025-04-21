# Add this to the end of /Users/alexeygerasymov/Documents/Repos/Python100/Tests/TestIter.py

print("\n--- Accumulate Example (Running Balance) ---")
from itertools import accumulate
import operator # For functions like mul, max etc.

"""
Running Balance:

- We simulate bank transactions (positive for deposits, negative for withdrawals).
- accumulate(transactions, initial=initial_balance) starts with the initial_balance and then adds each transaction sequentially, yielding the balance after each step.
- We iterate through the original transactions and the corresponding balances (offset by one due to the initial value) to show the state after each transaction.
"""

def show_running_balance(transactions, initial_balance=0):
    """
    Calculates and displays the running balance after a series of transactions.

    Args:
        transactions (list): A list of numbers representing deposits (+) or withdrawals (-).
        initial_balance (int/float): The starting balance.
    """
    # accumulate defaults to summation.
    # 'initial' provides the starting value before the first transaction.
    running_totals = list(accumulate(transactions, initial=initial_balance))

    print(f"Initial Balance: {running_totals[0]}")
    print("----------------------")
    print("Transaction | New Balance")
    print("----------------------")
    # running_totals[i+1] is the balance *after* transactions[i]
    for i, transaction in enumerate(transactions):
        new_balance = running_totals[i+1]
        # Basic formatting for alignment
        print(f"{transaction:11d} | {new_balance}")
    print("----------------------")

# --- Example Usage ---
daily_transactions = [100, -50, 200, -120, 30, -40]
show_running_balance(daily_transactions, initial_balance=500)


print("\n--- Accumulate Example (Running Maximum) ---")

"""
Running Maximum:

- We track the maximum temperature recorded.
- accumulate(values, func=max) calculates the maximum value seen so far at each step.
- We use operator.max (or simply max) as the function.
- We iterate through the original values and the corresponding maximum values to show the state after each measurement.We track the highest temperature seen so far in a list of daily temperatures.
accumulate(values, func=max) applies the max function cumulatively. For each element, it yields the maximum value between the accumulated maximum so far and the current element.
- We zip the original values and the running maximums to display them side-by-side.
"""

def track_running_maximum(values):
    """
    Calculates the running maximum value in a sequence.

    Args:
        values (list): A list of numbers.
    """
    # Use operator.max (or simply max) as the function
    running_max = list(accumulate(values, func=max)) # Could also use func=operator.max

    print(f"Original Values: {values}")
    print(f"Running Maximum: {running_max}")
    print("----------------------")
    print("Value | Running Max")
    print("----------------------")
    for value, current_max in zip(values, running_max):
         print(f"{value:5d} | {current_max}")
    print("----------------------")

# --- Example Usage ---
temperatures = [15, 18, 17, 22, 20, 25, 23]
track_running_maximum(temperatures)

# Example with cumulative product (like factorial if starting near 1)

"""
Cumulative Product:

Shows how to use a different function (operator.mul for multiplication). When applied to [1, 2, 3, 4, 5], it effectively calculates the factorials (1!, 2!, 3!, 4!, 5!).
"""

print("\n--- Accumulate Example (Cumulative Product) ---")
numbers_to_multiply = [1, 2, 3, 4, 5]
cumulative_product = list(accumulate(numbers_to_multiply, func=operator.mul))
print(f"Numbers: {numbers_to_multiply}")
print(f"Cumulative Product (Factorials): {cumulative_product}")

"""
Explanation of Changes:

- Renamed Function: Renamed to show_running_balance_non_negative to distinguish it from the original (if you keep both).
- Initial Balance Check: Added a check to ensure the initial_balance isn't negative, resetting it to 0 if it is, as a negative starting balance violates the non-negative rule.
- Custom Accumulation Function (add_with_floor):
    This nested function takes the current_balance (accumulated so far) and the next transaction.
    It calculates the potential_new_balance.
    Crucially, it returns max(0, potential_new_balance). This means if the sum is positive, it returns the sum; if the sum is negative, it returns 0.
- Using func in accumulate: We pass our add_with_floor function to the func argument of accumulate. Now, instead of just adding, accumulate uses our custom logic for each step.
- Example Usage: Added new examples specifically designed to show cases where the balance would have gone negative but is now floored at 0.
This approach keeps the concise structure provided by accumulate while incorporating the specific business rule (non-negative balance).
"""

def show_running_balance_non_negative(transactions, initial_balance=0):
    """
    Calculates and displays the running balance after a series of transactions,
    ensuring the balance never drops below zero.

    Args:
        transactions (list): A list of numbers representing deposits (+) or withdrawals (-).
        initial_balance (int/float): The starting balance. Must be non-negative.
    """
    if initial_balance < 0:
        print("Warning: Initial balance cannot be negative. Setting to 0.")
        initial_balance = 0

    # Define a custom accumulation function
    def add_with_floor(current_balance, transaction):
        """Adds transaction, but ensures result is not less than 0."""
        potential_new_balance = current_balance + transaction
        return max(0, potential_new_balance) # Return 0 if sum is negative

    # Use the custom function with accumulate
    running_totals = list(accumulate(
        transactions,
        func=add_with_floor, # Use our custom function
        initial=initial_balance
    ))

    print(f"Initial Balance: {running_totals[0]}")
    print("----------------------")
    print("Transaction | New Balance")
    print("----------------------")
    # running_totals[i+1] is the balance *after* transactions[i]
    for i, transaction in enumerate(transactions):
        new_balance = running_totals[i+1]
        # Basic formatting for alignment
        print(f"{transaction:11d} | {new_balance}") # Using 'd' assumes integer balances
        # If you expect floats, use 'f' or general formatting:
        # print(f"{transaction:11.2f} | {new_balance:.2f}")
    print("----------------------")

# --- Example Usage ---
daily_transactions_orig = [100, -50, 200, -120, 30, -40]
print("Original behavior (can go negative):")
# Assuming the original function is still available or renamed for comparison
# show_running_balance(daily_transactions_orig, initial_balance=500) # Original call

print("\nNon-negative behavior:")
show_running_balance_non_negative(daily_transactions_orig, initial_balance=500)

print("\nNon-negative behavior (starting low):")
# This transaction list would normally go negative quickly
low_start_transactions = [20, -50, 10, -100, 30]
show_running_balance_non_negative(low_start_transactions, initial_balance=10)

# Example with negative initial balance (will be reset to 0)
print("\nNon-negative behavior (negative initial balance):")
show_running_balance_non_negative([10, -5, 20], initial_balance=-100)

# --- Keep the rest of the file (Running Maximum, Cumulative Product) as is ---
# ... (rest of the code for track_running_maximum and cumulative product) ...


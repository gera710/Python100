from functools import reduce
import operator # For common operations like add, mul
import math     # For math.nan and math.isnan

# --- Reduce Example (Aggregating Processed Data) ---
print("\n--- Reduce Example (Aggregating Processed Data) ---")

# Scenario: You have a list of numerical data (e.g., the Fahrenheit temperatures
# that might be produced by a function like clean_convert_celsius_to_fahrenheit)
# and you want to aggregate them into a single summary value.

# Let's use a sample list of Fahrenheit temperatures (similar to what map might produce)
fahrenheit_temps = [77.9, 64.4, 86.36, 60.44, 71.78]
print(f"Sample Fahrenheit temperatures: {fahrenheit_temps}")

# --- 1. Summing all temperatures ---
# The function for reduce takes two arguments:
# - accumulator: the accumulated value from the previous step
# - current_element: the next element from the iterable

# Using a lambda function for addition:
# reduce(function, iterable)
sum_of_temps = reduce(lambda accumulated_sum, current_temp: accumulated_sum + current_temp, fahrenheit_temps)

# Alternatively, using operator.add for conciseness and potentially better performance:
# sum_of_temps_op = reduce(operator.add, fahrenheit_temps)

print(f"\nSum of all Fahrenheit temperatures: {sum_of_temps:.2f}")
# How it works for fahrenheit_temps = [77.9, 64.4, 86.36, 60.44, 71.78]:
# 1. accumulated_sum = 77.9 (first item), current_temp = 64.4 (second item)
#    lambda(77.9, 64.4) returns 77.9 + 64.4 = 142.3
# 2. accumulated_sum = 142.3, current_temp = 86.36
#    lambda(142.3, 86.36) returns 142.3 + 86.36 = 228.66
# 3. accumulated_sum = 228.66, current_temp = 60.44
#    lambda(228.66, 60.44) returns 228.66 + 60.44 = 289.1
# 4. accumulated_sum = 289.1, current_temp = 71.78
#    lambda(289.1, 71.78) returns 289.1 + 71.78 = 360.88
# Final result: 360.88

# Using an initializer: reduce(function, iterable, initializer)
# The initializer is used as the first 'accumulated_sum'.
sum_with_initializer = reduce(lambda acc, val: acc + val, fahrenheit_temps, 1000)
print(f"Sum with initializer 1000: {sum_with_initializer:.2f}") # 1000 + 360.88 = 1360.88

# --- 2. Finding the maximum temperature ---
# We need a function that returns the greater of two values.
def find_max_temp(temp1, temp2):
    # print(f"Comparing {temp1} and {temp2}") # Uncomment to see steps
    return temp1 if temp1 > temp2 else temp2

max_temp = reduce(find_max_temp, fahrenheit_temps)

# Alternatively, using a lambda:
# max_temp_lambda = reduce(lambda t1, t2: t1 if t1 > t2 else t2, fahrenheit_temps)
# Or even simpler with the built-in max function (which can act as a binary function here):
# max_temp_builtin = reduce(max, fahrenheit_temps)

print(f"\nMaximum Fahrenheit temperature: {max_temp}") # Expected: 86.36

# --- 3. Handling potential errors or filtering within the reduce logic ---
# Let's say our temperature list might contain non-numeric data or NaNs
# (Not a Number), which could come from failed conversions in a previous step.
temperatures_with_issues = [77.9, 64.4, "error_data", float('nan'), 86.36, 60.44, 71.78]
print(f"\nTemperatures with potential issues: {temperatures_with_issues}")

def safe_sum_temps(accumulator, current_value):
    """Adds current_value to accumulator if it's a valid number, otherwise keeps accumulator."""
    if isinstance(current_value, (int, float)) and not math.isnan(current_value):
        return accumulator + current_value
    else:
        print(f"Skipping invalid data: {current_value}")
        return accumulator # Return the accumulator unchanged

# It's crucial to provide an initializer (e.g., 0.0 for a sum) when the first
# element(s) of the iterable might be invalid, or if the iterable could be empty.
# Otherwise, if the first element is invalid, it might be passed as the initial accumulator.
sum_of_valid_temps = reduce(safe_sum_temps, temperatures_with_issues, 0.0)
print(f"Sum of valid temperatures (ignoring errors and NaN): {sum_of_valid_temps:.2f}")
# Expected: 77.9 + 64.4 + 86.36 + 60.44 + 71.78 = 360.88

# --- Edge Cases ---
# Reducing an empty list without an initializer raises a TypeError
try:
    reduce(operator.add, [])
except TypeError as e:
    print(f"\nError reducing empty list without initializer: {e}")

# Reducing an empty list with an initializer returns the initializer
sum_of_empty_with_init = reduce(operator.add, [], 0) # Initializer is 0
print(f"Sum of empty list with initializer 0: {sum_of_empty_with_init}") # Output: 0

# Reducing a list with one item without an initializer returns that item
single_item_list = [100]
result_single = reduce(operator.add, single_item_list)
print(f"Reduce on single item list [100]: {result_single}") # Output: 100

print("\n--- End of Reduce Example ---")

"""
Explanation of functools.reduce():

`functools.reduce(function, iterable[, initializer])`

1.  **Purpose**:
    `reduce` (also known as fold or accumulate) is a higher-order function. It applies a
    binary `function` (a function that takes two arguments) cumulatively to the items of
    an `iterable`, from left to right, to reduce the iterable to a single accumulated value.

2.  **How it Works**:
    *   **Without `initializer`**:
        *   The `function` is first called with the first two items from the `iterable`.
        *   The result of this call becomes the first argument (the "accumulator") for the
            next call, and the third item from the `iterable` becomes the second argument.
        *   This process continues until all items in the `iterable` have been processed.
        *   If the `iterable` is empty, a `TypeError` is raised.
        *   If the `iterable` has only one item, that item is returned without calling the function.
    *   **With `initializer`**:
        *   The `initializer` value is used as the first "accumulator".
        *   The `function` is first called with the `initializer` and the first item from
            the `iterable`.
        *   The result then becomes the accumulator for the next call with the second item,
            and so on.
        *   If the `iterable` is empty, the `initializer` is returned.

3.  **`function` Argument**:
    This must be a function that accepts two arguments. The first argument is the
    accumulated value from the previous step (or the initializer), and the second is the
    current item from the iterable. It should return the new accumulated value.

4.  **Common Use Cases**:
    *   Summing or multiplying all elements in a sequence (e.g., `reduce(operator.add, numbers)`).
    *   Finding the maximum or minimum element (e.g., `reduce(max, numbers)`).
    *   Flattening a list of lists (though other methods like list comprehensions or `itertools.chain`
        are often clearer).
    *   Implementing logical operations like `all` or `any` (e.g., `reduce(operator.and_, booleans)`).
    *   Any operation where you need to "roll up" or "accumulate" values from a sequence
        into a single result based on a pairwise operation.

5.  **Readability**:
    While powerful, `reduce` can sometimes make code harder to read for simple operations
    where dedicated built-in functions exist (e.g., `sum()`, `max()`, `min()`, `all()`, `any()`).
    It shines when the accumulation logic is more complex and doesn't have a direct built-in
    equivalent. For many transformations, list comprehensions or explicit loops might be
    preferred for clarity if `reduce` becomes too convoluted.
"""

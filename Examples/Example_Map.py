import math

print("\n--- Map Example (Cleaning and Converting Input Data) ---")

# Scenario: You receive a list of strings representing temperature readings,
# but they might have extra whitespace and need to be converted to floats
# for calculations. You also want to convert them from Celsius to Fahrenheit.

raw_temperatures_celsius = [" 25.5 ", "18.0", " 30.2 ", "15.8", "22.1 "]

print(f"Raw input data (strings): {raw_temperatures_celsius}")

# --- Step 1: Define the transformation function ---
# This function will perform multiple steps on a single item:
# 1. Remove leading/trailing whitespace (.strip())
# 2. Convert the cleaned string to a float (float())
# 3. Convert Celsius to Fahrenheit ((c * 9/5) + 32)

def clean_convert_celsius_to_fahrenheit(temp_str: str) -> float:
    """Cleans a temperature string, converts to float, and converts C to F."""
    try:
        cleaned_str = temp_str.strip()
        celsius = float(cleaned_str)
        fahrenheit = (celsius * 9/5) + 32
        return round(fahrenheit, 2) # Round for cleaner output
    except ValueError:
        print(f"Warning: Could not convert '{temp_str}'. Skipping.")
        # Return a value indicating an issue, like NaN (Not a Number)
        return math.nan # Or None, or raise an exception depending on needs

# --- Step 2: Use map() to apply the function to each item ---
# map(function, iterable) applies 'function' to every item in 'iterable'.
# It returns a map object, which is an iterator.
temperatures_fahrenheit_iterator = map(clean_convert_celsius_to_fahrenheit, raw_temperatures_celsius)

# The map object is lazy - it doesn't compute the values until you iterate over it.
print(f"\nType of map() result: {type(temperatures_fahrenheit_iterator)}")

# --- Step 3: Consume the iterator to get the results ---
# Convert the iterator to a list to see all the results at once.
# This is where the clean_convert_celsius_to_fahrenheit function is actually called for each item.
temperatures_fahrenheit_list = list(temperatures_fahrenheit_iterator)

print(f"\nProcessed temperatures (Fahrenheit, floats): {temperatures_fahrenheit_list}")
# Expected Output: Processed temperatures (Fahrenheit, floats): [77.9, 64.4, 86.36, 60.44, 71.78]

# --- Comparison with List Comprehension (often more 'Pythonic') ---
# The same result can often be achieved more concisely with a list comprehension.
print("\n--- Comparison with List Comprehension ---")

# We can reuse the function or embed the logic directly
processed_temps_lc = [clean_convert_celsius_to_fahrenheit(t) for t in raw_temperatures_celsius]
# Or directly:
# processed_temps_lc_direct = [round((float(t.strip()) * 9/5) + 32, 2) for t in raw_temperatures_celsius if t.strip()] # Added check

print(f"Result using list comprehension: {processed_temps_lc}")

# --- Example with multiple iterables (less common, often zip is clearer) ---
print("\n--- Map with Multiple Iterables (Simple Example) ---")
# Apply a function taking two arguments to elements from two lists
list_a = [1, 2, 3, 4]
list_b = [10, 20, 30, 40]

# Use map with a lambda function taking two arguments
sums_iterator = map(lambda x, y: x + y, list_a, list_b)
print(f"Sums of corresponding elements: {list(sums_iterator)}") # Output: [11, 22, 33, 44]

print("\n--- End of map Examples ---")

"""
Explanation:

1.  **Scenario:** 
The example tackles a realistic data preparation task: taking messy string inputs, 
cleaning them, converting their type, and performing a calculation (Celsius to Fahrenheit).

2.  **Transformation Function:** 
A dedicated function (`clean_convert_celsius_to_fahrenheit`) encapsulates 
the logic needed for *one* item. This makes the code modular and readable. 
It also includes basic error handling.

3.  **`map()` Application:** 
`map()` is used to apply this transformation function systematically to *every* string 
in the `raw_temperatures_celsius` list.

4.  **Iterator Result:** 
`map()` returns an *iterator*. This is memory-efficient, especially for large datasets, 
as it processes items one by one as needed, rather than creating the entire result list in memory upfront. 
We convert it to a `list()` only to display the full result easily.

5.  **Comparison:** 
The example shows the equivalent operation using a list comprehension. 
List comprehensions are often preferred in Python for their readability 
when the transformation logic is relatively simple. 
`map()` can be useful when you already have a complex function defined elsewhere or 
when working in a more functional programming style.

6.  **Multiple Iterables:** 
A brief example shows how `map` can take a function requiring N arguments and apply it to N iterables, 
processing corresponding elements until the *shortest* iterable is exhausted (similar to `zip`).

This example demonstrates `map`'s core purpose: 
applying a specific operation to each element of an iterable, 
producing a new iterable with the transformed results.
"""

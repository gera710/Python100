# --- Example: Using zip to Combine Related Data ---

# Imagine you have separate lists containing related information.
# For example, student names, their corresponding scores on a test,
# and the activities they participated in.

student_names = ["Alice", "Bob", "Charlie", "David"]
test_scores = [85, 92, 78, 88]
activities = ["Debate Club", "Chess Club", "Art Club", "Soccer Team"]

# --- Basic Zipping ---
# zip() takes iterables (like lists) and aggregates elements
# from each based on their position (index).
# It returns an iterator that yields tuples.

print("1. Zipping Names and Scores:")
zipped_data = zip(student_names, test_scores)

# The result is an iterator, so we convert it to a list to see all results at once
zipped_list = list(zipped_data)
print(f"   Zipped (Names, Scores): {zipped_list}")
# Output: Zipped (Names, Scores): [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 88)]

print("\n   Iterating through zipped data:")
# You can directly iterate over the zip object (more memory efficient for large data)
for name, score in zip(student_names, test_scores):
    print(f"   - {name} scored {score}")

# --- Zipping Multiple Iterables ---
print("\n2. Zipping Names, Scores, and Activities:")
combined_info = zip(student_names, test_scores, activities)

print("   Combined Student Info:")
for name, score, activity in combined_info:
    print(f"   - Name: {name}, Score: {score}, Activity: {activity}")

# --- Handling Unequal Lengths ---
# zip() stops as soon as the *shortest* input iterable is exhausted.

print("\n3. Zipping with Unequal Lengths:")
short_list = [1, 2]
long_list = ['a', 'b', 'c', 'd']

zipped_unequal = zip(short_list, long_list)
print(f"   Zipped (Short, Long): {list(zipped_unequal)}")
# Output: Zipped (Short, Long): [(1, 'a'), (2, 'b')]
# Notice 'c' and 'd' from long_list are ignored because short_list ended.

# If you need to include all elements, padding with a default value,
# use itertools.zip_longest
from itertools import zip_longest

print("\n4. Using zip_longest for Unequal Lengths:")
zipped_longest = zip_longest(short_list, long_list, fillvalue="N/A")
print(f"   zip_longest result: {list(zipped_longest)}")
# Output: zip_longest result: [(1, 'a'), (2, 'b'), ('N/A', 'c'), ('N/A', 'd')]


# --- Creating Dictionaries with zip ---
# A common use case is creating a dictionary from two lists (keys and values).
print("\n5. Creating a Dictionary from Zipped Data:")
keys = ["product_id", "name", "price"]
values = ["P101", "Laptop", 1200.00]

# Ensure lists have the same length for a direct mapping
if len(keys) == len(values):
    product_dict = dict(zip(keys, values))
    print(f"   Product Dictionary: {product_dict}")
    # Output: Product Dictionary: {'product_id': 'P101', 'name': 'Laptop', 'price': 1200.0}
else:
    print("   Cannot create dict: Key and value lists have different lengths.")


# --- Unzipping ---
# You can reverse the zip operation using zip with the * operator (unpacking)
print("\n6. Unzipping Data:")
zipped_pairs = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
print(f"   Original zipped pairs: {zipped_pairs}")

# *zipped_pairs unpacks the list into separate arguments for zip:
# zip(('Alice', 85), ('Bob', 92), ('Charlie', 78))
names, scores = zip(*zipped_pairs)

print(f"   Unzipped Names: {names}")   # Output is a tuple
print(f"   Unzipped Scores: {scores}") # Output is a tuple
# Output:
#    Unzipped Names: ('Alice', 'Bob', 'Charlie')
#    Unzipped Scores: (85, 92, 78)

print("\n--- End of zip Examples ---")

"""
Explanation of the Example:
1. Core Idea: 
The primary example shows combining parallel lists (student_names, test_scores, activities) 
where each element at a specific index corresponds to the elements at the same index in the other lists.

2. Basic Zipping: Demonstrates the fundamental use of zip with two lists and 
shows how to consume the resulting iterator (by converting to a list or iterating directly).

3. Multiple Iterables: Extends the concept to zip three lists simultaneously.

4. Unequal Lengths: Crucially highlights that zip stops when the shortest input iterable runs out. 
This is a common source of bugs if not understood.

5. zip_longest: Introduces the alternative from itertools for cases where you need 
to process all elements from the longest iterable, using a fillvalue for missing elements 
in shorter iterables.

6. Dictionary Creation: Shows a very practical application of zip – 
creating a dictionary directly from lists of keys and values.

7. Unzipping: 
Demonstrates the technique using zip(*...) to reverse the process, 
separating the aggregated tuples back into distinct tuples of related elements.
"""
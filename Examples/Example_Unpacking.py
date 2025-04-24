print("--- Unpacking Examples ---")

# ==============================================================================
# 1. Unpacking in Function Calls (*args) - Passing sequence elements as positional arguments
# ==============================================================================
print("\n1. Unpacking sequence into function arguments (*args):")

def calculate_average(student_name, *scores):
    """Calculates the average of provided scores."""
    print(f"  Calculating average for: {student_name}")
    if not scores:
        print("  No scores provided.")
        return 0
    print(f"  Scores received: {scores}") # scores is a tuple inside the function
    average = sum(scores) / len(scores)
    print(f"  Average score: {average:.2f}")
    return average

math_scores = [85, 92, 78, 90]
science_scores = (95, 88) # Works with tuples too

# Instead of calculate_average("Alice", 85, 92, 78, 90)
calculate_average("Alice", *math_scores)
# Instead of calculate_average("Bob", 95, 88)
calculate_average("Bob", *science_scores)
calculate_average("Charlie") # No scores passed

# Using print with unpacking
print("\n   Using print with unpacking:")
letters = ['a', 'b', 'c']
print("   Without unpacking:", letters) # Prints the list representation
print("   With unpacking:", *letters)    # Equivalent to print('a', 'b', 'c')

# ==============================================================================
# 2. Unpacking in Function Calls (**kwargs) - Passing dictionary items as keyword arguments
# ==============================================================================
print("\n2. Unpacking dictionary into function keyword arguments (**kwargs):")

def create_user_profile(username, email, **details):
    """Creates a user profile string with required and optional details."""
    print(f"  Creating profile for: {username} ({email})")
    print(f"  Additional details received: {details}") # details is a dict
    profile = f"User: {username}\nEmail: {email}"
    if details:
        profile += "\nDetails:"
        for key, value in details.items():
            profile += f"\n  - {key.replace('_', ' ').title()}: {value}"
    print(profile)
    print("-" * 20)

user_info = {
    "email": "david@example.com",
    "location": "New York",
    "join_date": "2023-10-27"
}
required_info = {"username": "david_r", "phone_number": "123-456-7890"}

# Instead of create_user_profile(username="david_r", email="david@example.com", location="New York", join_date="2023-10-27")
# Note: The keys in the dictionary must match the parameter names.
create_user_profile(**required_info, **user_info) # Combine multiple dictionaries

# Keys must match parameter names exactly
config_options = {
    "username": "test_user",
    "email_address": "test@example.com", # This key doesn't match 'email' parameter
    "theme": "dark"
}
try:
    # This will likely fail because 'email_address' is not 'email'
    print("  Attempting call with mismatched key:")
    create_user_profile(**config_options)
except TypeError as e:
    print(f"  Caught expected error: {e}")


# ==============================================================================
# 3. Unpacking in Assignments (Basic)
# ==============================================================================
print("\n3. Unpacking in variable assignments (Basic):")

coordinates = (10.0, 25.5) # Latitude, Longitude
latitude, longitude = coordinates
print(f"  Latitude: {latitude}, Longitude: {longitude}")

# Works with lists too
dimensions = [100, 50, 25] # Length, Width, Height
try:
    length, width = dimensions # Fails - too many values
except ValueError as e:
    print(f"  Caught expected error: {e}")

length, width, height = dimensions
print(f"  Dimensions: L={length}, W={width}, H={height}")

# Swapping variables using unpacking
a, b = 5, 10
print(f"  Before swap: a={a}, b={b}")
a, b = b, a # Elegant swap
print(f"  After swap: a={a}, b={b}")

# ==============================================================================
# 4. Unpacking in Assignments (Starred Expressions *)
# ==============================================================================
print("\n4. Unpacking in assignments with * (Starred Expressions):")

scores = [95, 88, 72, 90, 85]

# Get the first score and the rest
first_score, *remaining_scores = scores
print(f"  First score: {first_score}")
print(f"  Remaining scores: {remaining_scores}")

# Get the first, last, and middle scores
first, *middle, last = scores
print(f"  First: {first}, Middle: {middle}, Last: {last}")

# Get only the first two, ignore the rest
score1, score2, *_ = scores # Use *_ to indicate ignoring the rest
print(f"  First two scores: {score1}, {score2}")

# Get only the last one
*_, last_score = scores
print(f"  Last score: {last_score}")

# ==============================================================================
# 5. Unpacking for Merging Iterables and Dictionaries
# ==============================================================================
print("\n5. Unpacking for merging lists, tuples, sets, and dictionaries:")

# Merging Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, 0, *list2] # Creates a new list
print(f"  Merged list: {merged_list}")

# Merging Tuples
tuple1 = ('a', 'b')
tuple2 = ('c', 'd')
merged_tuple = (*tuple1, *tuple2)
print(f"  Merged tuple: {merged_tuple}")

# Merging Sets (automatically handles duplicates)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
merged_set = {*set1, *set2}
print(f"  Merged set: {merged_set}")

# Merging Dictionaries (Python 3.5+)
# Later keys overwrite earlier keys if they are the same
default_config = {"theme": "light", "font_size": 12, "show_sidebar": True}
user_config = {"font_size": 14, "language": "en"}

# User config overrides defaults where keys overlap
final_config = {**default_config, **user_config}
print(f"  Default config: {default_config}")
print(f"  User config: {user_config}")
print(f"  Final config: {final_config}")

# Order matters for overwriting
reversed_merge_config = {**user_config, **default_config}
print(f"  Reversed merge: {reversed_merge_config}")

# ==============================================================================
# 6. Unpacking in Loops
# ==============================================================================
print("\n6. Unpacking within loops:")

# Iterating over dictionary items
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print("  Student Grades:")
for student, grade in student_grades.items(): # .items() yields (key, value) tuples
    print(f"    - {student}: {grade}")

# Iterating with enumerate
items = ["apple", "banana", "cherry"]
print("  Items with index:")
for index, item in enumerate(items): # enumerate yields (index, value) tuples
    print(f"    {index}: {item}")

# Iterating with zip
names = ["John", "Jane", "Peter"]
ages = [30, 25, 35]
print("  Names and Ages:")
for name, age in zip(names, ages): # zip yields (item_from_names, item_from_ages) tuples
    print(f"    {name} is {age} years old.")

print("\n--- End of Unpacking Examples ---")

"""
Explanation of Examples:

1. *args in Function Calls: 

Shows how to pass elements from a list or tuple (math_scores, science_scores) as 
individual positional arguments to a function (calculate_average). 
Also demonstrates the common print(*iterable) pattern.

2. **kwargs in Function Calls: 

Demonstrates passing key-value pairs from dictionaries (user_info, required_info) as 
keyword arguments to a function (create_user_profile). 
Highlights that dictionary keys must match parameter names and shows 
how later dictionaries overwrite earlier ones if keys clash. 
Includes error handling for mismatched keys.

3. Basic Assignment Unpacking: 

Assigning elements of tuples/lists directly to variables (latitude, longitude = coordinates). 
Shows the requirement for the number of variables to match the number of elements and 
the classic variable swap idiom.

4. Starred Expressions (*) in Assignments: 

Using * to capture multiple items into a single list during assignment. 
Shows how to get the first/last elements and the rest (first, *rest), 
or the first/last and the middle (first, *middle, last), or how to ignore parts (*_).

5. Merging Collections: 

Using * to combine lists, tuples, and sets into new collections. 
Using ** to merge dictionaries, illustrating how key collisions are handled (last one wins). 
This is a very common pattern for combining data or setting defaults.

6. Unpacking in Loops: 

Implicit unpacking happens frequently in for loops when iterating over structures that yield tuples, 
like dict.items(), enumerate(), and zip(). This makes accessing the individual components within 
the loop very clean.
"""
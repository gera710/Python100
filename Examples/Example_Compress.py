print("\n--- Compress Example (Filtering with Selectors) ---")
from itertools import compress

# --- Example 1: Filtering Active Users ---
all_users = ["Alice", "Bob", "Charlie", "David", "Eve"]
activity_status = [True, False, True, True, False] # Bob and Eve are inactive

# compress yields items from 'all_users' where 'activity_status' is True
active_users_iterator = compress(all_users, activity_status)

print(f"All users:        {all_users}")
print(f"Activity status:  {activity_status}")
print(f"Active users only: {list(active_users_iterator)}")


# --- Example 2: Selecting Data based on a Condition ---
data_points = [15, 8, 22, 10, 19, 5, 11]
# Create selectors based on a condition (e.g., value > 10)
# Selectors can be any iterable yielding truthy/falsy values (True/False, 1/0)
is_greater_than_10 = [val > 10 for val in data_points] # [True, False, True, False, True, False, True]

selected_data_iterator = compress(data_points, is_greater_than_10)

print(f"\nData points:      {data_points}")
print(f"Is > 10?          {is_greater_than_10}")
print(f"Selected data (>10): {list(selected_data_iterator)}")

# --- Example 3: Using 0s and 1s as selectors ---
grades = ['A', 'C', 'B', 'F', 'B', 'A']
passed_exam = [1, 1, 1, 0, 1, 1] # 1 for pass, 0 for fail

passing_grades_iterator = compress(grades, passed_exam)
print(f"\nGrades:           {grades}")
print(f"Passed (1/0):     {passed_exam}")
print(f"Passing grades:   {list(passing_grades_iterator)}")

"""
Explanation:

1. Active Users: 
    We have a list of all_users and a parallel list activity_status indicating 
    if each user is active (True) or inactive (False). 
    compress(all_users, activity_status) iterates through both lists simultaneously. 
    It yields a user from all_users only if the corresponding value in activity_status is True.

2. Selecting Data: 
    We have data_points. We generate a selectors list (is_greater_than_10) dynamically 
    based on whether each data point meets a condition (> 10). 
    compress then uses this generated list to filter the original data_points.

3. 0s and 1s: 
    This shows that the selectors don't strictly need to be True/False. 
    Any value that Python considers "truthy" (like 1) or "falsy" (like 0) will work. 
    Here, we filter grades based on whether the student passed (1) or failed (0).

compress provides a concise and efficient way to perform filtering 
when you have a separate boolean mask or selection criteria aligned with your data.
"""

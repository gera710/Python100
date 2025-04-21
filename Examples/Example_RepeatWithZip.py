"""
Explanation:

We define a list of tasks.
We want to assign a default_priority (e.g., "Medium") to each task.
repeat("Medium") creates an iterator that will yield "Medium" endlessly (or until zip stops).
zip(tasks, repeat("Medium")) pairs the first task with "Medium", the second task with "Medium", and so on, until all tasks are processed.
list(...) consumes the zip iterator to create the final list of tuples.
The second example shows how easily you can change the repeated constant value.
The third example shows using the times argument of repeat to create a list of a specific size filled with a default value.
"""

print("\n--- Repeat Example (with zip) ---")
from itertools import repeat, zip_longest # zip also works, zip_longest handles unequal lengths if needed

def assign_default_priority(items, default_priority="Medium"):
    """
    Pairs each item in a list with a default priority level.

    Args:
        items (list): A list of items (e.g., tasks, products).
        default_priority (any): The constant value to pair with each item.

    Returns:
        list: A list of tuples, where each tuple is (item, default_priority).
    """
    # repeat(default_priority) generates the priority value for each item in 'items'
    # zip stops when the shortest iterator ('items' in this case) is exhausted.
    items_with_priority = list(zip(items, repeat(default_priority)))
    return items_with_priority

# --- Example Usage ---
tasks = ["Review PR", "Update Docs", "Fix Bug #123"]
tasks_prioritized = assign_default_priority(tasks)
print("Tasks with default priority:")
for task, priority in tasks_prioritized:
    print(f"- {task}: {priority}")

# You can specify a different constant value
tasks_high_priority = assign_default_priority(tasks, default_priority="High")
print("\nTasks assigned 'High' priority:")
print(tasks_high_priority)

# Another common use: creating a list/tuple of a fixed size with a default value
# (Though often list multiplication like [0] * 5 is simpler for immutable types)
default_settings = list(repeat(0, 5)) # Create a list of five zeros
print(f"\nList initialized with repeat: {default_settings}")


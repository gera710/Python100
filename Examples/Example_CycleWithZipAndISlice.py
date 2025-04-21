# Add this to the end of /Users/alexeygerasymov/Documents/Repos/Python100/Tests/TestIter.py

print("\n--- Cycle Example (Round-Robin Assignment) ---")
from itertools import cycle, islice 
# islice is useful for taking a limited number from an infinite iterator

def assign_round_robin(items, assignees) -> list:
    """
    Assigns items to assignees in a round-robin (cycling) fashion.

    Args:
        items (list): A list of items to assign (e.g., tasks, requests).
        assignees (list): A list of assignees to cycle through (e.g., workers, servers).

    Returns:
        list: A list of tuples, where each tuple is (item, assignee).
                 Returns empty list if assignees is empty.
    """
    if not assignees:
        print("Warning: No assignees provided.")
        return []
    # cycle(assignees) will yield 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', ...
    assignee_cycler = cycle(assignees)
    # zip pairs items with the next available assignee from the cycle
    # zip stops when the shortest iterable (items in this case) is exhausted.
    assignments = list(zip(items, assignee_cycler))
    return assignments

# --- Example Usage ---
tasks = [
    "Design Homepage",
    "Implement Login",
    "Write API Docs",
    "Setup Database",
    "Test Checkout",
    "Deploy to Staging",
    "User Acceptance Testing"
]
team_members = ["Alice", "Bob", "Charlie"]

task_assignments = assign_round_robin(tasks, team_members)
print("Task Assignments (Round-Robin):")
for task, member in task_assignments:
    print(f"- '{task}' assigned to {member}")

# Example showing how cycle continues indefinitely
# We can use islice to take just a few elements from the infinite cycle
print("\nFirst 10 assignments if tasks kept coming (using islice):")
assignee_generator = cycle(team_members)
first_10_assignees = list(islice(assignee_generator, 10))
# Note: islice consumes the generator, so assignee_generator is now advanced
print(first_10_assignees)

# Example with alternating styles
print("\nAlternating Row Styles:")
styles = ["light-row", "dark-row"]
style_cycler = cycle(styles)
data_rows = ["Row 1 Data", "Row 2 Data", "Row 3 Data", "Row 4 Data", "Row 5 Data"]

styled_rows = list(zip(data_rows, style_cycler))
for data, style_class in styled_rows:
    print(f'<div class="{style_class}">{data}</div>')


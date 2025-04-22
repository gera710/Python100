'''
Explanation:

- Scenario: We have tasks categorized into different priority lists (high_priority_tasks, medium_priority_tasks, low_priority_tasks). 
We want to iterate through all tasks sequentially, starting with high priority, then medium, then low.
- chain(high_priority, medium_priority, low_priority): This creates an iterator. When you iterate over all_tasks_iterator:
    - It first yields all elements from high_priority_tasks.
    - Once those are exhausted, it yields all elements from medium_priority_tasks.
    - Finally, it yields all elements from low_priority_tasks.
- Memory Efficiency: Importantly, chain does not create a new list containing all the tasks combined. It iterates through the original lists one by one, making it memory-efficient, especially if the lists are very large.
- Flexibility: It works with any kind of iterable (lists, tuples, strings, generators, etc.) and handles empty iterables correctly.
- String Example: The last part shows a simple case of chaining strings to iterate over all their characters sequentially.
'''
print("\n--- Chain Example (Processing Tasks from Different Lists) ---")
from itertools import chain

def process_all_tasks(high_priority, medium_priority, low_priority):
    """
    Processes tasks from different priority lists as a single sequence.

    Args:
        high_priority (iterable): Tasks with high priority.
        medium_priority (iterable): Tasks with medium priority.
        low_priority (iterable): Tasks with low priority.
    """
    print("Processing all tasks in order of priority lists:")
    # chain treats the lists as one continuous sequence: high -> medium -> low
    all_tasks_iterator = chain(high_priority, medium_priority, low_priority)

    for i, task in enumerate(all_tasks_iterator):
        # Simulate processing each task
        print(f"  Processing task {i+1}: {task}")

# --- Example Usage ---
high_priority_tasks = ["Fix critical bug #101", "Respond to urgent customer inquiry"]
medium_priority_tasks = ("Update documentation", "Refactor login module", "Plan next sprint") # Example with a tuple
low_priority_tasks = ["Organize project files", "Research new libraries"]
empty_priority_tasks = [] # Chain handles empty iterables gracefully

process_all_tasks(high_priority_tasks, medium_priority_tasks, low_priority_tasks)

print("\nProcessing with an empty list included:")
process_all_tasks(high_priority_tasks, empty_priority_tasks, medium_priority_tasks)

# Another common use: iterating over characters of multiple strings
print("\nChaining strings:")
string1 = "abc"
string2 = "DEF"
string3 = "123"
chained_chars = chain(string1, string2, string3)
print(f"Chained characters: {list(chained_chars)}")


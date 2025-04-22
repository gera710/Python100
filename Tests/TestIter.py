r = range(1, 11)
print(r)
print(r.__iter__)
print(iter(r))
print(list(r))
print(list(iter(r)))

i = iter(r)
print(next(i)) #1
print(next(i)) #2
print(i.__next__()) #3
print(next(i)) #4
print(i)
print(list(i))
#print(next(i)) - StopIteration

print("Iter functions")
from itertools import count, cycle, repeat

def count_example(start, step):
    counter = count(start, step)
    for number in counter:
        if number > 10:
            break
        print(number, end=' ')

count_example(1, 2)
print("Count End")

def repeat_example(text, times):
    repeater = repeat(text, times)
    print(repeater)
    for item in repeater:
        print(item)

repeat_example('A', 3)
print("Repeat End")

def cycle_example(items):
    cyc = cycle(items)
    for _ in range(5):
        print(next(cyc), end=' ')
        #print(next(cyc), end=' ')

cycle_example(['A', 'B', 'C'])
print("\nCycle End")

from itertools import chain, accumulate

def accumulate_example(numbers):
    acc = accumulate(numbers)
    print(acc)
    print(list(acc))

accumulate_example([1,2,3,4,5])
print("Accumulate End")

def chain_example(items1, items2):
    chain_items = chain(items1, items2)
    print(chain_items)
    print(list(chain_items))

chain_example([1,2,3], [4,5,6])
print("Chain End")

print("\n--- Chain Example (Multiple Iterables) ---")
# chain is useful for combining multiple iterables into one
# (without creating a new list in memory)
def chain_multiple_iterables(*iterables):
    """
    Chains multiple iterables together.

    Args:
        *iterables: Any number of iterable objects (lists, tuples, etc.).

    Returns:
        list: A list containing all elements from all iterables, in order.
    """
    chained_items = chain(*iterables)
    return list(chained_items)

# --- Example Usage ---
list1 = [1, 2, 3]
list2 = [4, 5]
tuple1 = (6, 7, 8)
string1 = "abc"
dict = {"d":9, "e":10}

combined_list = chain_multiple_iterables(list1, list2, tuple1, string1, dict.values(), dict.keys())
print(f"Combined list: {combined_list}")

# Example with empty iterables
empty_list = []
combined_with_empty = chain_multiple_iterables(list1, empty_list, list2)
print(f"Combined with empty list: {combined_with_empty}")



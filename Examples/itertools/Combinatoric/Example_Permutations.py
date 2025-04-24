print("\n--- Permutations Example (Order Matters) ---")
from itertools import permutations
import pprint # For potentially nicer printing of lists of tuples

# --- Example 1: Arranging Items in Sequence ---
items_to_arrange = ['A', 'B', 'C']
print(f"Items to arrange: {items_to_arrange}")

# Generate all possible unique orderings of the items
# r defaults to len(items_to_arrange), so permutations of length 3
all_arrangements_iterator = permutations(items_to_arrange)
all_arrangements = list(all_arrangements_iterator)

print("All possible arrangements (order matters):")
pprint.pprint(all_arrangements)
print(f"Total permutations: {len(all_arrangements)}") # Should be 3! = 3 * 2 * 1 = 6

# --- Example 2: Finding Anagrams (Permutations of letters) ---
word = "CAT"
print(f"\nWord: {word}")

# Generate permutations of the letters
letter_perms_iterator = permutations(word) # r defaults to len(word) = 3

# Join the characters in each permutation tuple back into a string
anagrams = [''.join(p) for p in letter_perms_iterator]

print(f"Possible arrangements (anagrams) of '{word}':")
print(sorted(anagrams)) # Sort for consistent display

# --- Example 2b: Word with repeated letters ---
word_repeated = "EVE"
print(f"\nWord with repeats: {word_repeated}")
letter_perms_repeated_iterator = permutations(word_repeated)
# Note: permutations treats elements by position. If input has duplicates,
# the output iterator will yield tuples that look identical but came from
# different original positions. Using set() on the final strings removes duplicates.
unique_anagrams_repeated = set(''.join(p) for p in letter_perms_repeated_iterator)
print(f"Unique arrangements of '{word_repeated}':")
print(sorted(list(unique_anagrams_repeated))) # EVE, EEV, VEE

# --- Example 3: Selecting and Arranging a Subset (using r) ---
candidates = ['Alice', 'Bob', 'Charlie', 'David']
num_positions = 2 # e.g., President and Vice-President (order matters)
print(f"\nCandidates: {candidates}")
print(f"Selecting for {num_positions} ordered positions.")

# Find all possible ways to choose 'num_positions' candidates AND assign them an order
ordered_selection_iterator = permutations(candidates, r=num_positions)
ordered_selections = list(ordered_selection_iterator)

print(f"Possible ordered selections for {num_positions} positions:")
pprint.pprint(ordered_selections)
print(f"Total ordered selections: {len(ordered_selections)}") # Should be P(4, 2) = 4! / (4-2)! = 4 * 3 = 12

print("\nNote: The number of permutations grows factorially (n!), becoming very large quickly.")

"""
Explanation:

1. Arranging Items: 
We have three items ['A', 'B', 'C']. permutations generates all 6 possible ways to order them: ('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), etc. This shows the fundamental concept where sequence is key.

2. Anagrams: 
We take the letters of the word "CAT". permutations generates all orderings of these letters (('C', 'A', 'T'), ('C', 'T', 'A'), etc.). We then use ''.join() to turn these tuples of characters back into strings, effectively finding all anagrams. The "EVE" example shows how to handle inputs with repeated elements if you only want the unique resulting strings.

3. Selecting and Arranging Subset (r): 
We have four candidates and want to choose two for specific, ordered positions (like President and VP). permutations(candidates, r=2) gives us all pairs where the order matters. ('Alice', 'Bob') is considered different from ('Bob', 'Alice'). This contrasts with combinations, where the order of selection doesn't matter.

These examples illustrate how permutations is used when the arrangement or sequence of elements is significant.
"""

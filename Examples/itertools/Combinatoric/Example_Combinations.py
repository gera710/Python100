print("\n--- Combinations Example (Order Does NOT Matter) ---")
from itertools import combinations
import pprint # For potentially nicer printing of lists of tuples
import math # To calculate expected number of combinations

# --- Example 1: Selecting a Committee ---
candidates = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
committee_size = 3
print(f"Candidates: {candidates}")
print(f"Selecting committees of size: {committee_size}")

# Generate all possible unique groups (committees) of size 'committee_size'
# Order doesn't matter: ('Alice', 'Bob', 'Charlie') is the same committee as ('Charlie', 'Bob', 'Alice')
committee_iterator = combinations(candidates, r=committee_size)
possible_committees = list(committee_iterator)

print(f"\nAll possible unique committees of size {committee_size}:")
pprint.pprint(possible_committees)

# Calculate expected number: C(n, r) = n! / (r! * (n-r)!)
n = len(candidates)
r = committee_size
expected_combinations = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
print(f"Total unique committees: {len(possible_committees)} (Expected C({n},{r}) = {expected_combinations})")


# --- Example 2: Selecting Pairs for Matches/Interactions ---
players = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
match_size = 2 # Selecting pairs
print(f"\nPlayers: {players}")
print(f"Selecting pairs for matches (size {match_size})")

# Generate all unique pairs of players for head-to-head matches
# ('Player 1', 'Player 2') is the same match as ('Player 2', 'Player 1')
match_pairs_iterator = combinations(players, r=match_size)
possible_matches = list(match_pairs_iterator)

print("\nAll possible unique match pairs:")
pprint.pprint(possible_matches)

n_players = len(players)
expected_pairs = math.factorial(n_players) // (math.factorial(match_size) * math.factorial(n_players - match_size))
print(f"Total unique pairs: {len(possible_matches)} (Expected C({n_players},{match_size}) = {expected_pairs})")


# --- Example 3: Choosing Ingredients ---
available_ingredients = ['Tomato', 'Cheese', 'Basil', 'Onion', 'Pepperoni']
pizza_ingredients_count = 3
print(f"\nAvailable Ingredients: {available_ingredients}")
print(f"Choosing {pizza_ingredients_count} ingredients for a pizza.")

# Generate all unique combinations of 3 ingredients
ingredient_combos_iterator = combinations(available_ingredients, r=pizza_ingredients_count)
possible_pizzas = list(ingredient_combos_iterator)

print(f"\nPossible {pizza_ingredients_count}-ingredient pizza combinations:")
pprint.pprint(possible_pizzas)
print(f"Total combinations: {len(possible_pizzas)}")

print("\nNote: Combinations are generated in lexicographical order based on the input iterable.")
print("Contrast with Permutations: In permutations, ('Alice', 'Bob') and ('Bob', 'Alice') are distinct.")
print("Contrast with Product: Product allows choosing the same item multiple times (if using repeat>1) and combines across different iterables.")

"""
Explanation:

1. Committee Selection: 
We have 5 candidates and want to form 3-person committees. combinations(candidates, 3) gives us all unique groups of 3. ('Alice', 'Bob', 'Charlie') is generated, but ('Bob', 'Alice', 'Charlie'), ('Charlie', 'Alice', 'Bob'), etc., are not generated because they represent the same group of people. The number of combinations follows the mathematical formula C(n, r).

2. Pairwise Matches: 
We have 4 players and want to find all unique pairs for matches. combinations(players, 2) generates pairs like ('Player 1', 'Player 2'), ('Player 1', 'Player 3'), etc. Again, ('Player 2', 'Player 1') is not generated as it's the same pair. This is useful for setting up round-robin tournament pairings or checking all possible interactions between pairs of items.

3. Choosing Ingredients: 
Similar to the committee example, we select 3 available_ingredients for a pizza. The order in which we pick them doesn't change the final set of ingredients on the pizza, so combinations is appropriate.

These examples highlight the core idea of combinations: selecting unique subsets where the internal order is irrelevant.
"""
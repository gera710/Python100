print("\n--- Product Example (Generating Combinations) ---")
from itertools import product
import pprint # For potentially nicer printing of lists of tuples

# --- Example 1: Generating Product Variations ---
sizes = ['S', 'M', 'L', 'XL']
colors = ['Red', 'Blue', 'Green']
styles = ['Crew Neck', 'V-Neck']

# Generate all possible T-shirt variations (Size, Color, Style)
# Equivalent to nested loops:
# for size in sizes:
#   for color in colors:
#       for style in styles:
#           print((size, color, style))

t_shirt_variations_iterator = product(sizes, colors, styles)

print(f"Sizes: {sizes}")
print(f"Colors: {colors}")
print(f"Styles: {styles}")
print("\nAll T-shirt variations (Size, Color, Style):")
# Convert to list for printing all at once, but product yields lazily
all_variations = list(t_shirt_variations_iterator)
pprint.pprint(all_variations, width=100)
print(f"Total variations: {len(all_variations)}") # len(sizes)*len(colors)*len(styles)


# --- Example 2: Parameter Grid for Testing/Simulation ---
learning_rates = [0.1, 0.01, 0.001]
batch_sizes = [32, 64]
optimizers = ['Adam', 'SGD']

# Generate all combinations of hyperparameters to test
parameter_grid_iterator = product(learning_rates, batch_sizes, optimizers)

print("\nHyperparameter Grid Search Combinations (Learning Rate, Batch Size, Optimizer):")
parameter_grid = list(parameter_grid_iterator)
pprint.pprint(parameter_grid)
print(f"Total parameter combinations: {len(parameter_grid)}")


# --- Example 3: Generating Coordinates or Dice Rolls (using repeat) ---
axes_coords = range(3) # Represents coordinates 0, 1, 2 on each axis
dimensions = 3

# Generate all points in a 3D grid (0,0,0) to (2,2,2)
# product(axes_coords, axes_coords, axes_coords)
grid_points_iterator = product(axes_coords, repeat=dimensions)

print(f"\nGrid points in {dimensions}D space with axis range {axes_coords}:")
grid_points = list(grid_points_iterator)
print(grid_points)

# Simulate rolling two 6-sided dice
die_faces = range(1, 7)
two_dice_rolls_iterator = product(die_faces, repeat=2)

print(f"\nAll possible outcomes of rolling two dice:")
two_dice_rolls = list(two_dice_rolls_iterator)
print(two_dice_rolls)
print(f"Total outcomes: {len(two_dice_rolls)}") # 6 * 6 = 36


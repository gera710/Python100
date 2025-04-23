print("\n--- chain.from_iterable Example (Flattening Grouped Data) ---")
from itertools import chain # Already imported, but good practice if standalone

def flatten_grouped_items(grouped_items):
    """
    Flattens an iterable where each element is itself an iterable
    (e.g., a list of lists, list of tuples) into a single sequence.

    Args:
        grouped_items (iterable): An iterable where each element is also iterable.

    Returns:
        list: A single list containing all items from the inner iterables.
    """
    print(f"Input grouped data: {grouped_items}")
    # chain.from_iterable takes ONE argument: an iterable (grouped_items)
    # where each element ('group') is itself iterable.
    flattened_iterator = chain.from_iterable(grouped_items)
    return list(flattened_iterator)

# --- Example Usage 1: List of Lists (e.g., sensor readings per batch) ---
sensor_batches = [
    [10.1, 10.2, 10.0], # Batch 1 readings
    [11.5, 11.6],       # Batch 2 readings
    [],                 # Batch 3 (empty)
    [9.8, 9.9, 10.0]    # Batch 4 readings
]
all_sensor_readings = flatten_grouped_items(sensor_batches)
print(f"All sensor readings (flattened): {all_sensor_readings}")

# --- Example Usage 2: List of Tuples (e.g., coordinates) ---
coordinate_pairs = [ (1, 2), (3, 4), (5, 6) ]
all_coordinates = flatten_grouped_items(coordinate_pairs)
print(f"All coordinates (flattened): {all_coordinates}")

# --- Example Usage 3: List of Strings (treats each string as an iterable of chars) ---
word_list = ["ABC", "DEF"]
all_characters = flatten_grouped_items(word_list)
print(f"All characters (flattened): {all_characters}")

# --- Comparison with chain(*iterable) ---
# You could achieve the same result for 'sensor_batches' using chain()
# by unpacking the outer list:
unpacked_chain_result = list(chain(*sensor_batches))
print(f"\nFlattened using chain(*sensor_batches): {unpacked_chain_result}")
# chain.from_iterable() is often more direct and readable when your input
# is already structured as a single iterable containing other iterables.
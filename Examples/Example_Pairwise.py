print("\n--- Pairwise Example (Calculating Differences & Path Segments) ---")
try:
    from itertools import pairwise # Requires Python 3.10+

    # --- Example 1: Calculating Differences between Consecutive Elements ---
    daily_temps = [15, 18, 17, 22, 20, 25, 23]
    print(f"Daily temperatures: {daily_temps}")

    # pairwise(daily_temps) yields (15, 18), (18, 17), (17, 22), ...
    # Calculate the change from the 'previous' day to the 'current' day
    temp_changes = [current - previous for previous, current in pairwise(daily_temps)]

    print(f"Daily temperature changes: {temp_changes}") # Output: [3, -1, 5, -2, 5, -2]

    # --- Example 2: Generating Segments from a Path ---
    route = ["Warehouse", "Hub A", "Customer 1", "Hub B", "Warehouse"]
    print(f"\nDelivery route: {route}")

    # pairwise(route) yields ('Warehouse', 'Hub A'), ('Hub A', 'Customer 1'), ...
    # These pairs represent the individual legs or segments of the journey
    route_segments = list(pairwise(route))

    print("Route segments (legs of the journey):")
    for start, end in route_segments:
        print(f"  - From '{start}' to '{end}'")

    # --- Example 3: Checking for strictly increasing sequence ---
    data_stream = [10, 12, 15, 15, 18, 20] # Not strictly increasing due to '15, 15'
    print(f"\nData stream: {data_stream}")

    # Check if 'a < b' holds true for all consecutive pairs (a, b)
    is_strictly_increasing = all(a < b for a, b in pairwise(data_stream))
    print(f"Is the stream strictly increasing? {is_strictly_increasing}") # False

    strictly_increasing_stream = [10, 12, 15, 17, 18, 20]
    print(f"\nData stream: {strictly_increasing_stream}")
    is_strictly_increasing_2 = all(a < b for a, b in pairwise(strictly_increasing_stream))
    print(f"Is the stream strictly increasing? {is_strictly_increasing_2}") # True

except ImportError:
    print("\nNote: itertools.pairwise requires Python 3.10 or later.")


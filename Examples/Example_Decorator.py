# Create a new file, e.g., /Users/alexeygerasymov/Documents/Repos/Python100/Examples/Example_Decorators.py

import time
import functools # Essential for writing well-behaved decorators
import logging
from typing import Callable, Any

# --- Setup Basic Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ==============================================================================
# 1. Logging Decorator
# ==============================================================================
def log_calls(func: Callable) -> Callable:
    """Decorator that logs when a function is entered and exited, along with args and result."""
    @functools.wraps(func) # Preserves original function metadata (name, docstring, etc.)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logging.info(f"Entering {func.__name__}({signature})")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Exiting {func.__name__} with result: {result!r}")
            return result
        except Exception as e:
            logging.exception(f"Exception in {func.__name__}: {e}")
            raise # Re-raise the exception after logging
    return wrapper

# ==============================================================================
# 2. Timing Decorator
# ==============================================================================
def time_execution(func: Callable) -> Callable:
    """Decorator that measures and prints the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # More precise than time.time() for duration
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        logging.info(f"Function {func.__name__} took {total_time:.4f} seconds to execute.")
        return result
    return wrapper

# ==============================================================================
# 3. Authorization Decorator (Simulated)
# ==============================================================================
# Simulate a global user context (in real apps, this might come from a request, session, etc.)
CURRENT_USER_PERMISSIONS = {'view', 'edit'}

def require_permission(required_permission: str) -> Callable:
    """
    Decorator factory that checks if the 'current user' has the required permission.
    Note: This takes an argument, so it requires an extra layer of nesting.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if required_permission in CURRENT_USER_PERMISSIONS:
                logging.info(f"Permission '{required_permission}' granted for {func.__name__}.")
                return func(*args, **kwargs)
            else:
                logging.warning(f"Permission '{required_permission}' denied for {func.__name__}.")
                # In a real app, you might raise an exception or return an error response
                raise PermissionError(f"User lacks required permission: '{required_permission}'")
        return wrapper
    return decorator # The factory returns the actual decorator

# ==============================================================================
# 4. Caching/Memoization Decorator
# ==============================================================================
def memoize(func: Callable) -> Callable:
    """Basic memoization decorator to cache results of function calls."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key from arguments (must be hashable)
        # Note: This simple key doesn't handle unhashable args like lists/dicts directly
        # or keyword argument order differences. More robust keys might be needed.
        key_args = tuple(args)
        key_kwargs = tuple(sorted(kwargs.items()))
        key = (key_args, key_kwargs)

        if key in cache:
            logging.info(f"Cache hit for {func.__name__} with key {key}")
            return cache[key]
        else:
            logging.info(f"Cache miss for {func.__name__} with key {key}. Computing...")
            result = func(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper


# --- Example Functions Using Decorators ---

@log_calls
def greet(name: str, greeting: str = "Hello") -> str:
    """A simple greeting function."""
    return f"{greeting}, {name}!"

@time_execution
def simulate_long_task(duration: float):
    """Simulates a task that takes time."""
    logging.info(f"Simulating work for {duration} seconds...")
    time.sleep(duration)
    logging.info("Simulation complete.")
    return "Task Finished"

@require_permission('edit')
@log_calls # Decorators stack - executed top-down at call time
def update_record(record_id: int, data: dict):
    """Simulates updating a record (requires 'edit' permission)."""
    print(f"  --> Actually updating record {record_id} with data {data}")
    return {"status": "success", "id": record_id}

@require_permission('admin') # This permission is not in CURRENT_USER_PERMISSIONS
def delete_system_file(filename: str):
    """Simulates a highly sensitive operation."""
    print(f"  --> Deleting system file {filename} !!!")
    return True

@memoize
@time_execution # Apply timing *before* memoization to see initial compute time
@log_calls
def slow_fibonacci(n: int) -> int:
    """Calculates Fibonacci numbers recursively (intentionally slow)."""
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n <= 1:
        return n
    else:
        # Recursive calls will also be logged and timed individually if not cached
        return slow_fibonacci(n-1) + slow_fibonacci(n-2)


# --- Running the Examples ---
print("\n--- Running Decorated Functions ---")

print("\n1. Testing @log_calls:")
greet("Alice")
greet("Bob", greeting="Hi")

print("\n2. Testing @time_execution:")
simulate_long_task(1.5)

print("\n3. Testing @require_permission and stacking:")
try:
    update_record(101, data={"value": 42})
except PermissionError as e:
    print(f"Caught expected error: {e}") # Should not happen as user has 'edit'

try:
    # This call should fail the permission check
    delete_system_file("/etc/important.conf")
except PermissionError as e:
    print(f"Caught expected error: {e}") # Should happen as user lacks 'admin'

print("\n4. Testing @memoize (and stacking):")
print("First call to slow_fibonacci(8):")
fib8_result1 = slow_fibonacci(8)
print(f"Result 1: {fib8_result1}")

print("\nSecond call to slow_fibonacci(8) (should be cached):")
fib8_result2 = slow_fibonacci(8)
print(f"Result 2: {fib8_result2}")

print("\nFirst call to slow_fibonacci(10):")
fib10_result1 = slow_fibonacci(10)
print(f"Result 1: {fib10_result1}")

print("\n--- End of Decorator Examples ---")

"""
Explanation:

1. @log_calls: 
When greet is called, the wrapper inside log_calls executes. 
It logs the entry message with arguments, calls the original greet, 
logs the exit message with the result, and returns the result.

2. @time_execution: 
The wrapper records the time before calling simulate_long_task, calls it, 
records the time after, calculates the difference, logs it, and returns the result.

3. @require_permission: 
This is a decorator factory. 
Calling @require_permission('edit') first calls require_permission with 'edit', 
which returns the actual decorator. This decorator then receives the update_record function. 
The wrapper inside checks CURRENT_USER_PERMISSIONS before deciding 
whether to call the original update_record or raise an error. 
Notice how delete_system_file fails because the user lacks the 'admin' permission.

4. @memoize: 
The wrapper creates a key based on the arguments passed to slow_fibonacci. 
If the key is in its cache dictionary, it returns the cached value immediately (cache hit). 
Otherwise, it calls the original slow_fibonacci (which is slow), stores the result in the cache, 
and then returns it (cache miss). Subsequent calls with the same arguments are much faster.

5. Stacking Decorators: 
When you stack decorators like on update_record or slow_fibonacci, 
they are applied from bottom up conceptually, but execute top-down at call time. 
For update_record:

    - A call first hits the require_permission wrapper.
    - If permission is granted, it calls the next wrapper, which is the log_calls wrapper.
    - The log_calls wrapper logs entry, calls the original update_record, logs exit, and returns.
    - The result bubbles back up through the wrappers.

6. functools.wraps: This is crucial. 
Without it, the decorated function (greet, simulate_long_task, etc.) would appear 
to be named wrapper and lose its original docstring, making debugging and introspection difficult. @wraps copies these essential attributes from the original function to the wrapper.
"""
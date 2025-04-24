import math

"""
Explanation:

1. __init__ (Constructor): Called when you create an object (Vector(x, y)). 
Initializes the object's state (setting self.x, self.y).

2. __repr__ (Representation): Provides the "official" string representation. 
Useful for debugging. Aims to be unambiguous.

3. __str__ (String): Provides the "user-friendly" string representation, used by print().

4. __add__, __sub__, __mul__ (Arithmetic Operators): 
Define what +, -, * mean for Vector objects. They check the type of the other operand and 
return a new Vector instance with the result, or 
NotImplemented if the operation isn't supported for that type combination.

5. __rmul__ (Reflected Multiplication): 
Handles cases like scalar * vector. Python tries scalar.__mul__(vector) first; 
if that's not implemented, it tries vector.__rmul__(scalar).

6. __eq__ (Equality): Defines how the == operator works. Compares the components of two vectors.

7. __abs__ (Absolute Value): Defines what abs(vector) does. 
Here, we use it for the vector's magnitude.

8. __bool__ (Boolean Value): Defines the truthiness of the object (e.g., in if vector:). 
True if it's not the zero vector.

9. __len__ (Length): Defines what len(vector) returns. Must be an integer. 
Here, it represents the number of dimensions (always 2).

10.__getitem__ (Indexing): Allows accessing parts of the object 
using square brackets (vector[0], vector[1]).

By implementing these dunder methods, the Vector class becomes much more intuitive and 
integrates seamlessly with Python's built-in operators and functions.

"""

class Vector:
    """
    Represents a 2D vector with x and y components.
    Demonstrates various dunder methods for custom behavior.
    """
    def __init__(self, x: float = 0, y: float = 0):
        """
        Initializes the vector.
        Called when you create an instance: Vector(3, 4)
        """
        self.x = float(x)
        self.y = float(y)
        print(f"  [__init__ called] Vector created: ({self.x}, {self.y})")

    # --- Representation Dunders ---
    def __repr__(self) -> str:
        """
        Returns the 'official' string representation of the object.
        Ideally, eval(repr(obj)) == obj.
        Called by repr(), often used in debugging and interactive sessions.
        """
        # Using !r ensures repr() is called on the attributes too
        return f"Vector({self.x!r}, {self.y!r})"

    def __str__(self) -> str:
        """
        Returns the 'informal' or user-friendly string representation.
        Called by str(), print(). Falls back to __repr__ if not defined.
        """
        return f"({self.x}, {self.y})"

    # --- Arithmetic Dunders ---
    def __add__(self, other):
        """
        Defines behavior for the '+' operator (self + other).
        """
        if isinstance(other, Vector):
            # Vector + Vector addition
            print(f"  [__add__ called] Adding {self} + {other}")
            return Vector(self.x + other.x, self.y + other.y)
        # Indicate that this operation is not implemented for other types
        print(f"  [__add__ called] Cannot add Vector and {type(other)}. Returning NotImplemented.")
        return NotImplemented

    def __sub__(self, other):
        """
        Defines behavior for the '-' operator (self - other).
        """
        if isinstance(other, Vector):
            print(f"  [__sub__ called] Subtracting {self} - {other}")
            return Vector(self.x - other.x, self.y - other.y)
        print(f"  [__sub__ called] Cannot subtract {type(other)} from Vector. Returning NotImplemented.")
        return NotImplemented

    def __mul__(self, scalar):
        """
        Defines behavior for the '*' operator (self * scalar).
        Typically used for scalar multiplication.
        """
        if isinstance(scalar, (int, float)):
            print(f"  [__mul__ called] Multiplying {self} * {scalar}")
            return Vector(self.x * scalar, self.y * scalar)
        print(f"  [__mul__ called] Cannot multiply Vector by {type(scalar)}. Returning NotImplemented.")
        return NotImplemented

    def __rmul__(self, scalar):
        """
        Defines behavior for reflected multiplication (scalar * self).
        Called if the left operand doesn't support __mul__ with the right operand.
        """
        print(f"  [__rmul__ called] Attempting reflected multiplication {scalar} * {self}")
        # Often, reflected operation is the same, so just call __mul__
        return self.__mul__(scalar)

    # --- Comparison Dunders ---
    def __eq__(self, other) -> bool:
        """
        Defines behavior for the equality operator '==' (self == other).
        """
        if isinstance(other, Vector):
            is_equal = (self.x == other.x) and (self.y == other.y)
            print(f"  [__eq__ called] Comparing {self} == {other}: {is_equal}")
            return is_equal
        print(f"  [__eq__ called] Cannot compare Vector and {type(other)}. Returning False.")
        return False # Or NotImplemented if you want Python to try other.__eq__(self)

    # --- Other Useful Dunders ---
    def __abs__(self) -> float:
        """
        Defines behavior for the built-in abs() function.
        Often used for magnitude or absolute value.
        """
        magnitude = math.sqrt(self.x**2 + self.y**2)
        print(f"  [__abs__ called] Calculating magnitude of {self}: {magnitude:.2f}")
        return magnitude

    def __bool__(self) -> bool:
        """
        Defines behavior when the object is used in a boolean context (e.g., if vector:).
        Called by bool(). Defaults to True if __len__ is not defined or returns non-zero.
        Commonly: True if non-zero/non-empty, False otherwise.
        """
        is_non_zero = self.x != 0 or self.y != 0
        print(f"  [__bool__ called] Checking boolean value of {self}: {is_non_zero}")
        return is_non_zero

    def __len__(self) -> int:
        """
        Defines behavior for the built-in len() function.
        MUST return an integer. Often represents size or number of components.
        """
        # For a 2D vector, we can say its "length" is its dimension count.
        print(f"  [__len__ called] Returning dimension count for {self}: 2")
        return 2

    def __getitem__(self, index: int):
        """
        Defines behavior for accessing items using square brackets (self[index]).
        """
        print(f"  [__getitem__ called] Accessing index {index} of {self}")
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range (must be 0 or 1)")


# --- Example Usage ---
print("--- Dunder Method Examples ---")

print("\n1. Initialization (__init__):")
v1 = Vector(3, 4)
v2 = Vector(1, -2)
zero_vector = Vector() # Uses default values

print("\n2. Representation (__str__ and __repr__):")
print(f"User-friendly (print v1): {v1}") # Calls __str__
print(f"Official (repr(v1)): {repr(v1)}") # Calls __repr__
print(f"In a list: {[v1, v2]}") # Containers typically use __repr__

print("\n3. Arithmetic (__add__, __sub__, __mul__, __rmul__):")
v_sum = v1 + v2
print(f"Result of v1 + v2: {v_sum}")
v_diff = v1 - v2
print(f"Result of v1 - v2: {v_diff}")
v_scaled = v1 * 3
print(f"Result of v1 * 3: {v_scaled}")
v_scaled_reflected = 0.5 * v2
print(f"Result of 0.5 * v2: {v_scaled_reflected}")

print("\n   Trying unsupported arithmetic:")
try:
    result = v1 + 10 # Vector + int is not implemented
except TypeError as e:
    print(f"   Caught expected error: {e}")

print("\n4. Comparison (__eq__):")
v3 = Vector(3, 4)
print(f"Is v1 == v2? {v1 == v2}")
print(f"Is v1 == v3? {v1 == v3}") # Same components
print(f"Is v1 == (3, 4)? {v1 == (3, 4)}") # Comparing with a different type

print("\n5. Built-in Functions (__abs__, __bool__, __len__):")
print(f"Magnitude of v1 (abs(v1)): {abs(v1):.2f}")
print(f"Magnitude of zero_vector (abs(zero_vector)): {abs(zero_vector):.2f}")
print(f"Boolean value of v1 (bool(v1)): {bool(v1)}")
print(f"Boolean value of zero_vector (bool(zero_vector)): {bool(zero_vector)}")
print(f"Length (dimensions) of v1 (len(v1)): {len(v1)}")

print("\n6. Item Access (__getitem__):")
print(f"X-component of v1 (v1[0]): {v1[0]}")
print(f"Y-component of v1 (v1[1]): {v1[1]}")

print("\n   Trying invalid index:")
try:
    component = v1[2]
except IndexError as e:
    print(f"   Caught expected error: {e}")

print("\n--- End of Dunder Examples ---")
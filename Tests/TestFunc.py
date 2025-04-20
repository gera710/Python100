from typing import List, Dict

def func(lst=[]):
    lst += [0]
    return lst
print(func())
print(func())
print(func())

def func1(*arg, **kwargs):
    print(arg)
    print(kwargs)

x = [1,2,3]
func1(*x, a=1, b=2)

def func2(x, y):
    print(x, y)

y = [(1,2), (3,4)]
func2(*y)

z = {"x":1, "y":2}
func2(**z)

def func3(*args, **kwargs) -> List[int]:
    """
    This function takes a list of integers and a dictionary of key-value pairs.
    It returns a list of integers.
    """
    combination: List[int] = []
    for arg in args:
        if isinstance(arg, int):
            combination.append(arg)

    for kwarg in kwargs.values():
        if isinstance(kwarg, int):
            combination.append(kwarg)

    return combination

test_list: List[int] = [1, 2, 3]
test_dict: Dict[str, int] = {"a": 4, "b": 5}

result: List[int] = func3(0, *test_list, 10, **{"m":15}, **test_dict)
print(result)
print(func3.__doc__)

import itertools
from typing import List, Any # Import Any for args/kwargs typing

def func3_refactored_concat(*args: Any, **kwargs: Any) -> List[int]:
    """
    Collects all integer values from positional and keyword arguments.

    Args:
        *args: Positional arguments.
        **kwargs: Keyword arguments.

    Returns:
        A list containing all integer values found in args and kwargs.values().
    """
    #int_args = [arg for arg in args if isinstance(arg, int)]
    #int_kwargs = [val for val in kwargs.values() if isinstance(val, int)]
    #return int_args + int_kwargs
    return [
        item for item in itertools.chain(args, kwargs.values())
        if isinstance(item, int)
    ]


# Example Usage (same as before)
test_list: List[int] = [1, 2, 3, "not_an_int"]
test_dict: Dict[str, Any] = {"a": 4, "b": 5, "c": "also_not_int"}

result: List[int] = func3_refactored_concat(0, *test_list, 10, **{"m":15}, **test_dict)
print(f"Refactored (concat) result: {result}")
print(func3_refactored_concat.__doc__)


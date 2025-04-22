def func(lst=[]):
    lst += [0]
    return lst
print(func())
print(func())
print(func())

"""
Default Mutable Arguments:

This code demonstrates a common Python "gotcha" related to default mutable arguments.

1. Default Argument Evaluation: 
    In Python, default arguments (like lst=[]) are evaluated only once, 
    when the function func is defined, not each time the function is called.

2.Creating the Default List: When the line def func(lst=[]): 
    is executed, Python creates a single empty list object [] in memory. 
    The default value for the parameter lst will always refer to this exact same list object 
    for all future calls to func that don't explicitly provide their own list.
3. First Call func():
    No argument is passed, so lst uses the default list object (which is currently []).
    lst += [0] modifies this default list in-place. The += operator on a list is equivalent 
    to the extend() method. So, the default list becomes [0].
    The function returns this modified list.
    Output: [0]
3. Second Call func():
    Again, no argument is passed. lst refers to the same default list object as before, 
    which is now [0].
    lst += [0] modifies this list again in-place. It becomes [0, 0].
    The function returns the modified list.
    Output: [0, 0]
4. Third Call func():
    No argument is passed. lst refers to the same default list object, which is now [0, 0].
    lst += [0] modifies it in-place to [0, 0, 0].
    The function returns the modified list.
    Output: [0, 0, 0]

The Key Takeaway:

    Because the default list [] is created only once and += modifies the list in-place, 
    subsequent calls to func without an argument operate on and modify the same list object, 
    leading to the accumulating effect seen in the output.

The Correct Idiom:

If the intention is to create a new empty list each time the function is called without an argument, 
the standard Python idiom is to use None as the default and create the list inside the function:

def func_corrected(lst=None):
    if lst is None:
        lst = []  # Create a new list if none was provided
    lst += [0]    # Or lst.append(0)
    return lst

print(func_corrected())  # Output: [0]
print(func_corrected())  # Output: [0]
print(func_corrected())  # Output: [0]

# You can still pass your own list
my_list = [1, 2]
print(func_corrected(my_list)) # Output: [1, 2, 0]
print(my_list)                 # Output: [1, 2, 0] (shows it was modified)
"""
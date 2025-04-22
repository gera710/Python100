def gen():
    for i in range(3):
        print(f"Y{i}", end=' ')
        yield i
def main():
    g = gen()
    x = next(g)
    y = sum(g)
    print(f"{x} {y}")

if __name__ == "__main__":
    main()

"""
Execution Flow and Output:

g = gen() creates the generator object.
x = next(g) runs gen until the first yield. It prints "Y0 " and x becomes 0.
y = sum(g) continues running gen from where it left off.
    It prints "Y1 ", yields 1.
    It prints "Y2 ", yields 2.
    The generator is exhausted.
    sum calculates 1 + 2 = 3. y becomes 3.
print(f"{x} {y}") prints the values of x and y.
Therefore, the final output of the script will be:
Y0 Y1 Y2 0 3
"""
"""
Detailed explanation:
def gen():
    # This defines a generator function. Code inside only runs when iterated over.
    for i in range(3): # Loop will run for i = 0, 1, 2
        print(f"Y{i}", end=' ') # Print "Y" followed by the current i value
        yield i # Pause execution and yield the current value of i

def main():
    # 1. Create the generator object. No code inside gen() runs yet.
    g = gen()

    # 2. Call next(g):
    #    - Execution enters gen().
    #    - Loop starts, i = 0.
    #    - print(f"Y{0}", end=' ') executes. Output: "Y0 "
    #    - yield 0 executes. The value 0 is returned by next().
    #    - Execution in gen() pauses *after* the yield 0.
    x = next(g) # x is assigned the value 0

    # 3. Call sum(g):
    #    - sum() iterates over the *remaining* items yielded by g.
    #    - Execution resumes in gen() *after* yield 0.
    #    - Loop continues, i = 1.
    #    - print(f"Y{1}", end=' ') executes. Output: "Y1 "
    #    - yield 1 executes. sum() receives the value 1.
    #    - Execution resumes in gen() *after* yield 1.
    #    - Loop continues, i = 2.
    #    - print(f"Y{2}", end=' ') executes. Output: "Y2 "
    #    - yield 2 executes. sum() receives the value 2.
    #    - Execution resumes in gen() *after* yield 2.
    #    - The loop finishes (range(3) is exhausted).
    #    - gen() finishes.
    #    - sum() calculates the total of values it received: 1 + 2 = 3.
    y = sum(g) # y is assigned the value 3

    # 4. Print the final result:
    #    - Prints the value of x (0) and y (3), separated by a space.
    print(f"{x} {y}") # Output: "0 3"
"""
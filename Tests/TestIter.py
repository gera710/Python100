r = range(1, 11)
print(r)
print(r.__iter__)
print(iter(r))
print(list(r))
print(list(iter(r)))

i = iter(r)
print(next(i)) #1
print(next(i)) #2
print(i.__next__()) #3
print(next(i)) #4
print(i)
print(list(i))
#print(next(i)) - StopIteration

print("Iter functions")
from itertools import count, cycle, repeat

def count_example(start, step):
    counter = count(start, step)
    for number in counter:
        if number > 10:
            break
        print(number, end=' ')

count_example(1, 2)
print("Count End")

def repeat_example(text, times):
    repeater = repeat(text, times)
    print(repeater)
    for item in repeater:
        print(item)

repeat_example('A', 3)
print("Repeat End")

def cycle_example(items):
    cyc = cycle(items)
    for _ in range(5):
        print(next(cyc), end=' ')
        #print(next(cyc), end=' ')

cycle_example(['A', 'B', 'C'])
print("\nCycle End")

from itertools import chain, accumulate

def accumulate_example(numbers):
    acc = accumulate(numbers)
    print(acc)
    print(list(acc))

accumulate_example([1,2,3,4,5])
print("Accumulate End")



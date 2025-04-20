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
print("Count")

def repeat_example(text, times):
    repeater = repeat(text, times)
    for item in repeater:
        print(item)

repeat_example('A', 3)
print("Repeat")
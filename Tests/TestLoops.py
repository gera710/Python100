for i in range(1, 10, 2):
    print(i, end=' ')

print()
x =[2,4,-5,10,1]

for i in x:
    print(i+1, end=' ')
    #print(i+1, end=' ')

print()
for i, elem in enumerate(x):
    print(i, elem)
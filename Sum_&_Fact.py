from time import *

def sum(A):
    add = 0
    if A == 1:
        return 1
    else:
        add = A + sum(A-1)
        return add
def factorial(A):
    fact = 0
    if A == 1:
        return 1
    else:
        fact = A * factorial(A-1)
        return fact

inp = int(input('Enter a positive number to find sum and factorial')) #input from user
if inp == 0:
    print("The sum is ZERO AND factorial is ONE")
elif inp == 1:
    print("The sum AND factorial both are 1")
elif inp > 1:
    print('The sum uptil 1 is -->', sum(inp))
    print('The factorial is -->', factorial(inp))
t = time()
print('Hah, done in', time()-t)



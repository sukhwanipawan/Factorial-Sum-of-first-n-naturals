def sum(A):
    add = 0
    if A == 1:
        return 1
    else:
        add = A + sum(A-1)
        return add


inp = int(input('Enter a positive number to find sum')) #input from user
if inp == 0:
    print("The sum is ZERO")
elif inp == 1:
    print("The sum is 1")
elif inp > 1:
    print(sum(inp))

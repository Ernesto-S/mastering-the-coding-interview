counter = 0

def inception():
    global counter
    if counter > 3:
        return 'Done'
    counter += 1
    return inception()

print(inception())

# Write two functions that finds the factorial of any number.One should use recursive, the other should just use a for loop.
N = 1
def find_factorial_recursive(n):
    global N
    if n == 2:
        return N
    N = N*n
    n -= 1
    return find_factorial_recursive(n)

def find_factorial_iterative(n):
    factorial = 1
    for i in range(2,n+1):
        factorial = factorial*i
    return factorial

print("Interactive")
print(find_factorial_iterative(5))
print("Recursive")
print(find_factorial_recursive(6))
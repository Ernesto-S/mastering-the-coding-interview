counter = 0

def inception():
    global counter
    if counter > 3:
        return 'Done'
    counter += 1
    return inception()

# print(inception())

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

# print("Interactive")
# print(find_factorial_iterative(5))
# print("Recursive")
# print(find_factorial_recursive(6))

# Given a number N return the index value of the Fibonacci sequence, where the sequence is:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# The pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 -> 2+3

def iterative_fibonacci(n):
    fib = [0, 1]
    
    for i in range(2, n+1):
        fib.append(fib[i-2]+fib[i-1])
    return fib[n]    

print(iterative_fibonacci(40))

fibonacci = 0
def recursive_fibonacci(n):
    global fibonacci
    if n < 2:
        return n
    
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

print(recursive_fibonacci(40))
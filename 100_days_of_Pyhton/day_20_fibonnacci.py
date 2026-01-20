# Fibonacci sequence
# Write a function to calculate the Fibonacci sequence up to a certain limit.

def Fib(n):
    seq = []
    a, b = 0, 1

    for i in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq


print(Fib(10))

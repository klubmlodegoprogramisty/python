def reccure_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return reccure_fibonacci(n - 1) + reccure_fibonacci(n - 2)

fibonacci = [ reccure_fibonacci(n) for n in range(20) ]
print(f"Fibonacci list: {fibonacci}")

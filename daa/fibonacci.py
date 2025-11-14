# Fibonacci (Non-Recursive)
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


# Fibonacci (Recursive)
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Driver Code
if __name__ == "__main__":
    n = 10  # Change for more terms

    # Iterative
    fib_iter = fibonacci_iterative(n)
    print("Iterative Fibonacci:", fib_iter)

    # Recursive
    fib_recur = [fibonacci_recursive(i) for i in range(n)]
    print("Recursive Fibonacci:", fib_recur)

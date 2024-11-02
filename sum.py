def sum_recursive(n):
    if n == 0:
        return 0  # Base case
    else:
        return n + sum_recursive(n - 1)  # Recursive call
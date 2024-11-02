def collatz_length(n):
    # Base case: if n reaches 1, the sequence stops
    if n == 1:
        return 1  # Only the number 1 itself counts as 1 step
    # Recursive case: if n is even, divide by 2
    elif n % 2 == 0:
        return 1 + collatz_length(n // 2)
    # Recursive case: if n is odd, apply 3n + 1
    else:
        return 1 + collatz_length(3 * n + 1)

# Example usage
n = 6
print("Length of the 3n+1 sequence starting from", n, ":", collatz_length(n))
# Define a global array
arr = [1, 2, 3, 4, 5]

# Recursive function to find the length of the global array
def recursive_length(index=0):
    global arr  # Declare that we are using the global array
    if index == len(arr):
        return 0  # Base case: reached the end of the array
    else:
        return 1 + recursive_length(index + 1)  # Count this element and move to the next

# Call the function and print the result
print("Length of the array:", recursive_length())
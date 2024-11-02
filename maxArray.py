# Recursive function to find the maximum in an array
def find_max_recursive(arr, index=0):
    # Base case: if there's only one element left, return it
    if index == len(arr) - 1:
        return arr[index]
    
    # Recursive call: get the maximum of the rest of the array
    max_in_rest = find_max_recursive(arr, index + 1)
    
    # Return the larger of the current element and the maximum of the rest
    return max(arr[index], max_in_rest)

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("Maximum element in the array:", find_max_recursive(arr))
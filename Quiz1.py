def binary_search_sequence(nums, target):
    l, r = 0, len(nums) - 1
    seq = []
    
    while l <= r:
        mid = l + (r - l) // 2
        seq.append(nums[mid])  # Append the middle element to seq
        
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return seq

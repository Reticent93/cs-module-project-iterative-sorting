def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1
    while start <= end:
        midpoint = (end + start) // 2
        # m_value = arr[midpoint]
        if target == arr[midpoint]:
            return midpoint
        elif target < arr[midpoint]:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return -1  # not found

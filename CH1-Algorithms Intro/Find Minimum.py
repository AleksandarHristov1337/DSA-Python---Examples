def find_minimum(nums):
    # Set minimum to positive infinity
    minimum = float("inf")
    # if list is empty return None
    if not nums:
        return None
    # Loop Try nums list
    for num in nums:
    # If minimum is bigger than num set new value eg: If 10 > 5 set it to 5
        if num < minimum:
            minimum = num
    
    return minimum

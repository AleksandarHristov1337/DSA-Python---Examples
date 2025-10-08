def find_max(nums):
    # First we check if nums is empty and if it is we return None
    if not nums:
        return None
    # We create a starting point in our list to check with other numbers for max value
    max_val = nums[0]
    # Since we already have first number in list in our  max_val = nums[0] or so we start from the next value to iterate over
    for num in nums[1:]:
        # Here we simply check if num in our list we iterate over is bigger than the max_val we have we set max_val with   
        # the bigger number we have in our list so for example if we have [1,2,3] first we check if 2 > 1 if it is we set it
        # to 2 if 3 > 2 we set it to 3 and we get the biggest number 
        if num > max_val:
            max_val = num
    return max_val

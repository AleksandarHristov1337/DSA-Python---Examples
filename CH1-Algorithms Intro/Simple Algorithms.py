def summed(nums):
    # Set a variable so we can track the total of all numbers in nums
    total = 0  
    # Loop try all numbers in nums and add them to total
    for num in nums:
        total += num  
    return total

#  return sum(nums) <--- We can also use the  built-in sum() and it will still work too in a single line
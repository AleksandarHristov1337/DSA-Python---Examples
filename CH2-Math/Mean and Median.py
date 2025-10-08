def average_followers(nums):
    # if the list is empty we return None
    if not nums:  
        return None
    # We initialise two variables to keep track
    total = 0
    count = 0
    # We do a loop to get all numbers from list
    for num in nums:
        # We get the total of all numbers here or simply said to calculate the average, you need the sum of all numbers.
        total += num  
        # then we add the count of all numbers in list to get the average
        count += 1    
    # to get the average we simply divide the total by the count of all numbers
    average = total / count 
    
    return average

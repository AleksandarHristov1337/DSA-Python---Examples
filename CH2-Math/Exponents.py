def get_estimated_spread(audiences_followers):
    # We create two variables to track total_followers and num_followers
    total_followers = 0
    num_followers = 0

    # We check if the list is empty and return 0
    if not audiences_followers:
        return 0
   
    # We add up all the followers numbers in the list
    for followers in audiences_followers:
        total_followers += followers
    
    # Here we iterate try the list to get the length of the list and add it to num_followers
    for num_followers_loop in audiences_followers:
        num_followers += 1
    
    # Here we get the average number of all followers
    average_audience_followers = total_followers / num_followers
    
    # We use this formula to get estimated spread by using the average of all followers and multiplying it by the exponent of num_followers of 1.2
    estimated_spread = average_audience_followers * (num_followers ** 1.2)
    
    return estimated_spread

# We can also solve the task by using the built in sum and len
# def get_estimated_spread(audiences_followers):
# If the list is empty, return 0
# if not audiences_followers:
#     return 0

# Calculate the average of the audience's followers
#  average_audience_followers = sum(audiences_followers) / len(audiences_followers)

# Calculate the number of followers (length of the audiences_followers list)
#   num_followers = len(audiences_followers)

# Apply the formula for estimated spread
#  estimated_spread = average_audience_followers * (num_followers ** 1.2)

#   return estimated_spread

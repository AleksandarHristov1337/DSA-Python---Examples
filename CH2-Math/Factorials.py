def num_possible_orders(num_posts):
    # To to build the factorial for example [total = 1 * 1 = 1] [total = 1 * 2 = 2] we use one because zero would lead to 
    # [total = 0 * 1 = 0] [total = 0 * 2 = 0] or so 
    total = 1
    
    # Here we use a range or so meaning we start from 1 and we go to the end of num_posts by using num_posts + 1
    # for example range(1, 4 + 1) where 4 is num_posts and we need to include the last value of num_posts that's why we do + 1
    # then to finish it off we do total which is for example if we have at start [3 , 5] we do 1 * 3 and after total is 3
    # we do 3 * 5 and we get 15 or so
    for i in range(1, num_posts + 1):
        total *= i 
    
    return total


# We can solve it using math.factorial too 
# import math

# def num_possible_orders(num_posts):
#   return math.factorial(num_posts)

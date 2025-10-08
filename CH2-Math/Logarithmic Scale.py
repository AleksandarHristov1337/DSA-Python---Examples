# Notice this is a brute force attempt and only would work correctly all the numbers are exact powers of the base.
# For example to reach the number 1 in list by multiplying it by 2 you need to do it 0 times for 2 for example you need to do it 1 time and so on
def log_scale(data, base):
    # Initialise empty list result[]
    result = []
    # Loop try all nums in data
    for num in data:
        # This will count how many times we multiply base.
        count = 0
        # We start multiplying from 1.
        # This variable will grow by being multiplied with base repeatedly.
        current = 1
        while current < num:
            # Multiply current by base.
            current *= base
            # Increase the counter — this keeps track of how many times you’ve multiplied.
            count += 1
            # Append count using float for not using whole numbers
        result.append(float(count))
    return result


# You can do it using math.log or so without brute forcing
# import math

# def log_scale(data, base):
# Create an empty list to store the log-scaled values
#  result = []

# Loop through each number in the data list
# for num in data:
        # Calculate the log of the number with the given base
#    log_value = math.log(num, base)
# Append the result to the new list
#   result.append(log_value)

# Return the list of log-scaled values
# return result

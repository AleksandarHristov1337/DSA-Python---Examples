def binary_search(target, arr):
    # We set two variables for the list length 0 the start and len(arr) the end
    low = 0
    high = len(arr) - 1
    # Here we check if high is bigger than low and if it is it means the list is empty
    while low <= high:
        # Here we get the middle index by using // we basically round up the number so if we have 7 elements we have 3 as middle
        mid = (low + high) // 2
        # This what it does basically is checks if we have found in lower code the  target if we haven't found it we
        # continue searching left or right
        guess = arr[mid]
        
        # if we get a match of the target and guess we print true
        if guess == target:
            return True
        # if the target is bigger than the guess at index 3 for example we set low index of = 0 to low = 4 and we continue and so on
        elif guess < target:
            low = mid + 1
        # if the target is smaller than the guess at index 3 for example we set the lenght of array to 2 as index so high ecomes = 2 and 
        # we continue and so on 
        else:
            high = mid - 1

    return False

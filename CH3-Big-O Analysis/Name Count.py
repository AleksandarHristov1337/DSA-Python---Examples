def count_names(list_of_lists, target_name):
    count = 0
    # Loop over each list in the nested list
    for sublist in list_of_lists:
        # Loop over each name in the current sublist
        for name in sublist:
            # If the name matches target_name, increment count
            if name == target_name:
                count += 1
    return count

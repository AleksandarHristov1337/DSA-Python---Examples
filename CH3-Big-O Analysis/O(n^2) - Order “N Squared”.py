def does_name_exist(first_names, last_names, full_name):
    # First we loop over the first names in the list
    for first in first_names:
    # Secondly we loop over the last names in the list
        for last in last_names:
    # We combine both of the first + last and then we check if it's equal to the full_name we have given
    # and if it is we return true otherwise it defaults to false
            if first + " " + last == full_name:
                return True
    return False

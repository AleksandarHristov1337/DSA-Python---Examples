def find_last_name(names_dict, first_name):
   # we get the key or so for example using dictionary and when we do "Alice" we get "Smith" no need for looping over the whole data with loops
   # {
   # "Alice": "Smith",
   # "Bob": "Johnson",
   # "Carol": "Davis"
   # }

     return names_dict.get(first_name)



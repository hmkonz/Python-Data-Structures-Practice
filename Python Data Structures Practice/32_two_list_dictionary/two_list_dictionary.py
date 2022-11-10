def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    dictionary = dict()

    if len(keys) <= len(values):
        # iterates as many times as the length of keys
        for item in range(len(keys)):
        # assigns keys[item] to the key and values[item] to the value in dictionary 
            dictionary[keys[item]] = values[item]

    elif len(keys) > len(values):
        # because there are less values than keys, we iterate as many times as the length of values and assign those pairs in dictionary
        for item in range(len(values)):
            dictionary[keys[item]] = values[item]
        # for the keys that don't have matching values (less values than keys), we iterate from a range with index = length of values to index = length of keys (those keys without values) and assign 'None' as the value of keys[item] in dictionary
        for item in range(len(values),len(keys)):
            dictionary[keys[item]] = None
     
    return dictionary
   

def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    # d.keys() retrieves all the keys from 'd' and creates a list i.e. [2, 7, 1, 10, 4]
    # min() and max() find the min and max keys from the list created by d.keys()
   
    return (min(d.keys()), max(d.keys()))
    


        
   
def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newList = []

    for elem in lst:
        if elem:
            newList.append(elem)

    return newList

    # OR
    # return [elem for elem in lst if elem]

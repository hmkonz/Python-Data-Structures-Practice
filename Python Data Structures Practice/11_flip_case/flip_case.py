def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # convert 'to_swap' to lower case for comparison purposes
    to_swap = to_swap.lower()
    # create new string
    newPhrase = ""
    # loop over each letter in 'phrase'
    for ltr in phrase:
    # if lower-cased ltr in 'phrase' equals lower-cased 'to_swap', swap the casing of ltr and add it to newPhrase
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        newPhrase += ltr

    return newPhrase



          
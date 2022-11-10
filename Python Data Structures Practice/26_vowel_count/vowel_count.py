def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    phrase = phrase.lower()
    counter = {}


# loop over letters in phrase
    for ltr in phrase:
        # check to see if 'ltr' is a vowel        
        if ltr in 'aeiou':
        # if 'ltr' is a vowel, increase the 'value' of the key 'ltr' by 1 if 'ltr' is in 'counter'. If ltr is not in 'counter', 'value' of 'ltr' is set equal to default value of zero and then 1 is added.
        # counter.get(ltr, 0) checks to see if the key 'ltr' exists in the dictionary 'counter'. If found, 1 is added to the 'value' of 'ltr'. If not found, its 'value' is set to default value of zero and then 1 is added.
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter
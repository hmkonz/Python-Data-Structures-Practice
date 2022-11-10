def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # makes all letters in phrase lower-case and removes all spaces
    new_Phrase = phrase.lower().replace (' ', '')
    # [::-1] reverses the order of the string from the end to the beginning
    # returns True of False if the reversed string equals the lower-case string with no spaces
    return new_Phrase == new_Phrase[::-1]

  
        

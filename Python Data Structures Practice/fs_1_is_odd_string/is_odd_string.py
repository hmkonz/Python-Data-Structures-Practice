def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

 

    # to find the char position, we'll change it's ordinal ASCII number into
    # a 1-based number ("a" = 1, "b" = 2). To do that, let's subtract
    # this from it

    total = 0
    
    DIFF = ord("a") - 1
    for char in word.lower():
        total = total + (ord(char) - DIFF)

    return total % 2 == 1
        

#   OR
        
    # DIFF = ord("a") - 1

    # total = sum((ord(c) - DIFF) for c in word.lower())

    # return total % 2 == 1


 # OR
 
 # using ordinal ASCII position 
    # char_position = 0

    # for char in word:
    #     char_position = char_position + ord(char)

    # if char_position%2 == 1:
    #      return True
    # else:
    #      return False
def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """


# convert string 's' to a list so can more easily manipulate it 
    string = list(s)
# set 'i' to be at the beginning of the list, set 'j' to be at the end of the list so can compare first letter with last letter, second letter with second to last letter, etc
    i = 0
    j = len(s) - 1
# loop over string until reach the middle of the string
    while i < j:
# if letter from the beginning is not a vowel, increment i and do nothing (skip over it)
        if string[i].lower() not in "aeiou":
            i += 1
# if letter from the end is not a vowel, decrement j and do nothing (skip over it)
        elif string[j].lower() not in "aeiou":
            j -= 1
        else:
# otherwise, assign letter at index i equal to letter at index j and vice versa (swap letters) and increment i and decrement j to move to the next letters
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
# turn list back into string
    return "".join(string)

def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

  


#   In Python you need to give access to a file by opening it. You can do it by using the 
#   open() function. Open returns a file object

#  A common way to work with files in Python is to create a file handler with an “open” statement
#  and work with the file. After finishing the work with the file, we need to close the file
#  handler. Often, it is hard to remember to close the file once we are done with the file.

#   The 'with' statement provides a way for ensuring that the file will automatically be closed. 
#   Once opened, files must be closed

#   Use 'file' as the file handler which refers to the file object
    with open(filename) as file:
        # iterate over each line in 'file'
        for line in file:
            # remove 'newline' (end-of-line character) at end of line
            line = line.strip()
            # print out each line separately with a "-" before it.
            print(f"- {line}")
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # for i in matrix:
    #     print(len(i))
    #     for j in range(len(i)):
    #         print(range(len(i)))
    #         sum = sum + num

    total = 0
    # loop from index of 0 to index of len of matrix
    for i in range(len(matrix)):
    # for i =0, matrix[i][i] retrieves the first number in first list (index 0,0) and adds it to total. for i=1, the second number in second list (index 1,1) is added to total, etc.
        total += matrix[i][i]
    # for i=0, matrix[i][-1 -1] retrieves the last number in first list (index 0,-1). for i=1, the second from the last number in second list (index 1, -2) is added total, etc 
        total += matrix[i][-1 - i]
        
    return total
        
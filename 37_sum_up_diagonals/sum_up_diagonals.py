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
    sum_of_TL_to_BR = 0
    sum_of_BL_to_TR = 0

    TL_to_BR_index = 0
    BL_to_TR_index = len(matrix) - 1

    for row in matrix:
        sum_of_TL_to_BR += row[TL_to_BR_index]
        sum_of_BL_to_TR += row[BL_to_TR_index]
        TL_to_BR_index += 1
        BL_to_TR_index -= 1

    return sum_of_TL_to_BR + sum_of_BL_to_TR
def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    list_of_digits_1 = [int(d) for d in str(num1)]
    list_of_digits_2 = [int(d) for d in str(num2)]

    list_of_digits_1.sort()
    list_of_digits_2.sort()

    if list_of_digits_1 == list_of_digits_2:
        return True
    else:
        return False
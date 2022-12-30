def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False

        >>> valid_parentheses("())(")
        False

        >>> valid_parentheses("())(()")
        False

        >>> valid_parentheses(")(")
        False

        >>> valid_parentheses("(((((()())))))()")
        True
    """
    par_dict = {'(': 1, ')':-1}
    check_sum = 0

    if len(parens)%2 != 0:
        return False
        # Odd number of parens is obviously not valid !!
        # If odd number of parens, we do not bother to check anything else
        # and immediately return False.
        # We only bother to process further even number of paren symbols
    else:
        for p in parens:
            if check_sum == 0 and p == ')': # Cannot lead with close-paren !!
                return False # WRONG ORDER !!
                # This checks if close-paren is being used when open-paren should be.
                # It invalidates situations like these ----> "())(" or ")()(" or ")("
            check_sum += par_dict[p]
        if check_sum == 0: # CORRECT ORDER !!
            # If check_sum == 0, this means that 
            # every open-paren has been paired with a corresponding close-paren
            return True
        else:
            return False
            # If check_sum is anything other than 0,
            # this means that one or more open-parens have not been closed
  
    
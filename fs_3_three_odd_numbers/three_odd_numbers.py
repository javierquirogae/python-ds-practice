def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    groups_of_3_to_check = len(nums) - 2
    summation = 0   
    if len(nums) == 3:
        for n in nums:
            summation += n
        if summation%2 != 0:
            return True
    else:
        for i in range(groups_of_3_to_check):
            summation = 0   
            for n in nums[i:i + 3]:
                summation += n
            if summation%2 != 0:
                # print(f"this is the odd one -> {summation}")
                return True 
            # print(f"summation -----------> {summation}")
    return False



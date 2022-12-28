def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    frequencies = [nums.count(n) for n in nums]
    max_frequency = 0
    
    for x in frequencies:
        if x > max_frequency:
            max_frequency = x
    index_of_max_frequency = frequencies.index(max_frequency)

    return nums[index_of_max_frequency]

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
    most_common = 0

    for num in nums:
        if nums.count(num)> most_common:
            most_common += 1
            return num

       
    # OR ?????
    # Make frequency counter of num:freq
    # counts = {}

    # for num in nums:
    #     counts[num] = counts.get(num, 0) + 1

    # # find the highest value (the most frequent number)

    # max_value = max(counts.values())

    # # now we need to see at which index the highest value is at

    # for (num, freq) in counts.items():
    #     if freq == max_value:
    #         return num

          

     


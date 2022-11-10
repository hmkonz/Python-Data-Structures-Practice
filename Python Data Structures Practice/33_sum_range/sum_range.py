def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    # nums = [1, 2, 3, 4]
    # sum =0
    
    # if start == 0 and end == None:
    #     for num in range(nums[::]):
    #         sum = sum + num
    # elif end != None and end < len(num):
    #     for num in range(start, end+1):
    #         sum = sum + num
    # elif end != None and end > len(num):
    #     for num in range(start, len(num)):
    #         sum = sum + num

    # return sum

    if end is None:
    # assign 'end' equal to the length of 'nums'
        end = len(nums)
    # 'sum' is a method that finds the sum of nums from 'start' to 'end+1'
    return sum(nums[start:end + 1]) 
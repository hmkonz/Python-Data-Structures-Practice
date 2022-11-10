def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    list_length = len(nums)
    repeated_nums = []
    # iterate as many times as the length of 'nums'
    for i in range(list_length):
    # add 1 to i for every iteration and set it equal to k. 
        k = i + 1
    # loop as many times as k (i + 1) to the length of 'nums'. This allows nums[i] to be compared against nums[i+1] for every iteration 
        for j in range(k, list_length):
    # append nums[i] to repeated_nums list if equal to next num (num[j]) and not already in repeated_nums (means it's a duplicate)
            if nums[i] == nums[j] and nums[i] not in repeated_nums:
                repeated_nums.append(nums[i])
    # retrieve and return num in repeated_nums
                return (repeated_nums.pop())
    # if no duplicates, repeated_nums will be [] so return None
    if repeated_nums == []:
             return None


 
 

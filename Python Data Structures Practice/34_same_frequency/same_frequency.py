def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    all_freq_num1 = {}
    all_freq_num2 = {}


    for nums1 in str(num1):
        if nums1 in all_freq_num1:
            all_freq_num1[nums1] += 1
        else:
            all_freq_num1[nums1] = 1 

    for nums2 in str(num2):
        if nums2 in all_freq_num2:
            all_freq_num2[nums2] += 1
        else:
            all_freq_num2[nums2] = 1 

    if all_freq_num1 == all_freq_num2:
        return True
    else:
        return False

# OR
# def freq_counter(coll):
    # """Returns frequency counter mapping of coll."""

    # counts = {}

    # for x in coll:
    #     counts[x] = counts.get(x, 0) + 1

    # return counts
    
# return freq_counter(str(num1)) == freq_counter(str(num2))
  
   
     
def string_interleave(s1, s2):
    """Interleave a character from a small string to a big string

    Args:
        s1 (str): input string
        s2 (str): input string

    Returns:
        (str): the string that already interleave

    Raises:
        TypeError: if s1 or s2 is not a string

    Examples:
    >>> string_interleave("abc", "mnopq")
    'manbocpq'
    >>> string_interleave("mnopq", "abc")
    'manbocpq'
    >>> string_interleave("Mine", "Thai")
    'TMhianie'
    >>> string_interleave("Theprove", "Puchonggggggggg")
    'PTuhcehpornogvgeggggggg'
    >>> string_interleave("itumelabmaidai", "mairooruengloei")
    'miatiurmoeolraubemnagildoaeii'
    >>> string_interleave(25269, "mnop")
    Traceback (most recent call last):
    ...
    TypeError: s1 is not a string
    >>> string_interleave("mnop", 25269)
    Traceback (most recent call last):
    ...
    TypeError: s2 is not a string
    """
    # raise error
    if type(s1) == int:
        raise TypeError("s1 is not a string")
    elif type(s2) == int:
        raise TypeError("s2 is not a string")
    # function program
    s1.split()
    s2.split()
    output = []
    if len(s1) > len(s2):
        for i in range(len(s2)):
            output.append(s1[i])
            output.append(s2[i])
        loop = len(s2) + 1
        while loop <= len(s1):
            output.append(s1[loop - 1])
            loop += 1
    else:
        for i in range(len(s1)):
            output.append(s2[i])
            output.append(s1[i])
        loop = len(s1) + 1
        while loop <= len(s2):
            output.append(s2[loop - 1])
            loop += 1
    ans = ""
    for k in range(len(output)):
        ans += output[k]
    return ans


def selective_sum(n, k):
    """Return the sum of the k largest digits of n

    Args:
        n (int): input integer
        k (int): input integer

    Returns:
        (int): the sum of the k largest digits of n

    Raises:
        ValueError: if k is negative
        TypeError: if n or k is not an integer
        OverflowError: if n or k is more than 1e30

    Examples:
    >>> selective_sum(3018, 2)
    11
    >>> selective_sum(593796, 3)
    25
    >>> selective_sum(12345, 10)
    15
    >>> selective_sum(888888, 3)
    24
    >>> selective_sum(9,10)
    9
    >>> selective_sum(4867, -9)
    Traceback (most recent call last):
    ...
    ValueError: k cannot be a negative integer
    >>> selective_sum("ilove", 5)
    Traceback (most recent call last):
    ...
    TypeError: n is not an integer
    >>> selective_sum(78346, "ajparuj")
    Traceback (most recent call last):
    ...
    TypeError: k is not an integer
    """
    # raise error
    if type(n) != int:
        raise TypeError("n is not an integer")
    elif type(k) != int:
        raise TypeError("k is not an integer")
    elif k < 0:
        raise ValueError("k cannot be a negative integer")
    elif n > 1e30:
        raise OverflowError('n is too large')
    elif k > 1e30:
        raise OverflowError('k is too large')
    # function program
    list_number = list(str(n))
    if len(list_number) > k:
        list_number.sort(reverse=True)
        for i in range(len(list_number)):
            list_number[i] = int(list_number[i])
        plus_list = []
        for i in range(k):
            plus_list.append(list_number[i])
        return sum(plus_list)
    else:
        for i in range(len(list_number)):
            list_number[i] = int(list_number[i])
        return sum(list_number)


def list_intersect(l1, l2):
    """Return the intersection list of l1 and l2

        Args:
            l1 (list): input list
            l2 (list): input list

        Returns:
            (list): the sum of the k largest digits of n

        Raises:
            TypeError: if l1 or l2 is not a list

        Examples:
        >>> list_intersect([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8])
        [1, 2, 3, 4]
        >>> list_intersect([5, 6, 7, 8], [1, 2, 3, 4])
        []
        >>> list_intersect([1, 2, 2, 3, 4, 5], [1, 2, 3, 4])
        [1, 2, 3, 4]
        >>> list_intersect([9, 10, 11, 12], [5, 6, 9, 10, 7, 8])
        [9, 10]
        >>> list_intersect(['Invoker', 'Lina', 'The Prove','Aghanim'], ['Lina', 'Zeus', 'Bloodseeker'])
        ['Lina']
        >>> list_intersect('Zezay', [54, 55, 66])
        Traceback (most recent call last):
        ...
        TypeError: l1 is not a list
        >>> list_intersect([54, 55, 58], 'Noboomta')
        Traceback (most recent call last):
        ...
        TypeError: l2 is not a list
        """
    # raise error
    if type(l1) != list and type(l2) != list:
        raise TypeError("l1 and l2 is not a list")
    elif type(l1) != list:
        raise TypeError("l1 is not a list")
    elif type(l2) != list:
        raise TypeError("l2 is not a list")
    # function program
    l1 = set(l1)
    l2 = set(l2)
    if len(l1) > len(l2):
        return list(l1 & l2)
    else:
        return list(l2 & l1)
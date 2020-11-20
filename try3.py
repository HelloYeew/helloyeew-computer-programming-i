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
    >>> string_interleave(25269, "mnop")
    Traceback (most recent call last):
    ...
    TypeError: s1 is not a string
    >>> string_interleave("mnop", 25269)
    Traceback (most recent call last):
    ...
    TypeError: s2 is not a string
    """
    if type(s1) == int:
        raise TypeError('s1 is not a string')
    if type(s2) == int:
        raise TypeError('s2 is not a string')
    s1.split()
    s2.split()
    listt = []
    if len(s1) > len(s2):
        for i in range(len(s2)):
            listt.append(s1[i])
            listt.append(s2[i])
        a = len(s1) - len(s2)
        for i in range(a):
            listt.append(s1[len(s2)+i])
    elif len(s2) > len(s1):
        for i in range(len(s1)):
            listt.append(s2[i])
            listt.append(s1[i])
        a = len(s2) - len(s1)
        for i in range(a):
            listt.append(s2[len(s1)+i])
    elif len(s1) == len(s2) :
        for i in range(len(s1)):
            listt.append(s2[i])
            listt.append(s1[i])
    printt = ""
    for i in range(len(listt)):
        printt += listt[i]
    return printt
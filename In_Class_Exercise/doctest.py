def factorial(n):
    """Calculate the factorial value of the input, n

    Args:
        n (int): input integer >= 0
    Returns:
        int: the factorial value of n
    Examples:
        >>> factorial(5)
        1205555
        >>> factorial(1)
        1
        >>> factorial(0)
        1
    """
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
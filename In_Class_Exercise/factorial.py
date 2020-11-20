def factorial(n):
    """Calculate the factorial of an integer input, n
    Args:
    n (int): input integer value >= 0
    Returns:
    int: the factorial value of n
    Raises:
    TypeError: if n is not an integer
    Exception: if n is negative
    Examples:
    >>> factorial(5)
    120
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(5.2)
    Traceback (most recent call last):
    ...
    TypeError: n is not integer; n value is 5.2 and n type is <class 'float'>
    >>> factorial(-6)
    Traceback (most recent call last):
    ...
    Exception: n must be greater than or equal to zero; n value is -6
    """
    if isinstance(n, int) == False:
        raise TypeError('n is not integer; n value is {} and n type is {}'.format(n, type(n)))
    if n < 0:
        raise Exception('n must be greater than or equal to zero; n value is {}'.format(n))
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
def make_square_dict(n):
    """Returns a dictionary that contains a sequence
    of key-value pairs in the form (x, x*x) where x ranges from 1 to n

    >>> make_square_dict(5)
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> make_square_dict(3)
    {1: 1, 2: 4, 3: 9}
    """
    dict = {}
    for i in range(1,n+1):
        dict[i] = i*i
    print(dict)

def make_color(n):
    dict = {}
    keys = ['red','green','blue']
    values = ['#FF0000','#008000','#0000FF']
    for i in range(n):
        dict[keys[i]] = values[i]
    print(dict)

make_color(3)
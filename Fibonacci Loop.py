def fib(n):
    """This function prints a Fibonacci sequence up to the nth Fibonacci
    """
    for loop in range(1,n+1):
        a = 1
        b = 1
        print(1,end="  ")
        if loop % 2 != 0:
            for i in range(loop // 2):
                print(a,end="  ")
                b = b + a
                print(b,end="  ")
                a = a + b
            print()
        else:
            for i in range((loop // 2) - 1):
                print(a,end="  ")
                b = b + a
                print(b,end="  ")
                a = a + b
            print(a,end="  ")
            print()

def fibo(n):
    """ accepts an in integer as input and returns
    the fibonacci number """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

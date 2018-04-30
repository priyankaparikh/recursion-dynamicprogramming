""" ways to get to stairs n """

def climbStairs(self, n):
    """ similar to fibonacci sequence """
    # f(n) = f(n-1) + f(n-2) + f(n-3)
    # empty array to store sequences
    seq = []

    for num in (0, 1, 2):
        steps[num] = num

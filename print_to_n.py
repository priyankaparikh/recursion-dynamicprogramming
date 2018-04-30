def tprint(i, n):
    
    if i > n:
        return
    print i
    tprint(i+1, n)

tprint(0, 50)

#loop through the string from the centre and outwards towards the first and last
# indices.
# keep checks for the even and odd counts for the center
# youtube tutorials https://www.youtube.com/watch?v=1iU-WXG-J_Y&index=4&list=PLFpmUCsiFBPlzlDuS20GYKvr83BKFi2bK

def get_longest(str, left, right):
    """ returns the index of the start and end of the longest palindrome.
     An even length palindrome always has two indices in the middle."""
    if right >=  len(str):
        return(0,0)

    start = left
    end = right

    while start >= 0 and end <= len(str) and str[start] == str[end]:
        start -= 1
        end += 1

    return (start + 1, end - 1) #decrement indices in the return statement

def longest(str):
    # initialize the start and end indices to zero
    start = 0
    end = 0

    for i in range(len(str)):
        left, right = get_longest(str, i)
        # when the lenght of the palindrome returned by the helper is greater
        # than the current function we update the start and end accordingly

        if right - left > end - start:
            start = left
            end = right

    return str[start:end +1]

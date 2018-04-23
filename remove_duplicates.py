# remove duplicates from a sorted array

def remove_dup(lst):
    if len(lst) <= 1:
        return len(lst)

    prv = lst[0]
    start = 0

    for i in range(1, len(lst)):
        if nums[i] != prv:
            start += 1
            lst[i], lst[start] = lst[start], lst[i]
            prv = lst[start]

    return start += 1

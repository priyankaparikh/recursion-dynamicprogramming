# reverse an integer without using extra memory or data structures
# youtube tutoria :https://www.youtube.com/watch?v=sIJtI5yFVgk&index=5&list=PLFpmUCsiFBPlzlDuS20GYKvr83BKFi2bK
# continuously take and remove the last digits and add them to out integers
# mutate the current integer using a custom algorithm
# getting the last digit  : take % 10
# removing the last  :  // 10
# adding the digit to the new int : * 10

def reverse_integer(x):
    rev= 0
    sign = 1 if x > 0 else -1 if x < 0
    tmp = x


    while temp != 0:
        rev = rev * 10 + tmp % 10
        tmp = tmp // 10

    return rev * sign

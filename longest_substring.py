def longest_sub_without_repeat(str):

    max_length = 0
    count = 1
    i = 0

    while i < len(str) - 1 :
        if str[i] != str[i + 1]:
            count += 1
            i += 1
        else:
            if max_length < count:
                max_length = count
                count = 1
                i += 1


    print count

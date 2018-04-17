# assuming that the characters are all ascii
# cracking the coding interview q1.1


def is_unique_chars(sr):

    if len(sr) > 128:
        return False

    else:
        char_check = [False] * 128

        for char in sr:
            if not char_check[ord(char)]:
                char_check[ord(char)] = True
            else:
                return False

        return True


print(is_unique_chars("hello"))
print(is_unique_chars("hi"))

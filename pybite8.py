def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    while n !=0:
        if (n<0):
            string = string[-1] + string[:-1]
            n += 1
        else:
            string = string[1:] +string[0]
            n -= 1
    return string



def rotate(string, n):
    return string[n:] + string[:n]
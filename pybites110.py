def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        int_num = int(numerator)
        int_den = int(denominator)
        ans = int_num/int_den
    except ZeroDivisionError:
        return 0
    except ValueError:
        raise
    else:
        return ans
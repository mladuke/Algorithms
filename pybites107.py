def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    return [i for i in numbers   if (int(i) % 2 == 0 and int(i)>0)]


numbers = list(range(-10, 11))
print(filter_positive_even_numbers(numbers))
# [2, 4, 6, 8, 10]

numbers = [2, 4, 51, 44, 47, 10]
print(filter_positive_even_numbers(numbers))
# [2, 4, 44, 10]

numbers = [0, -1, -3, -5]
print(filter_positive_even_numbers(numbers))
# []

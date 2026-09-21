def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    largest_num = numbers[0]

    for number in numbers:
        if number > largest_num:
            largest_num = number
    return largest_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))

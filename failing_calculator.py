def average_ratios(numbers):
    valid_numbers = [number for number in numbers if number != 0]

    if not valid_numbers:
        raise ValueError("At least one non-zero number is required.")

    total = sum(100 / number for number in valid_numbers)
    return total / len(valid_numbers)

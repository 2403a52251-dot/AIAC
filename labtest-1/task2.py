def sum_even_odd(numbers):
    """Return a tuple of (sum_of_even_numbers, sum_of_odd_numbers) from the list.

    Args:
        numbers: Iterable of integers.

    Returns:
        Tuple (even_sum, odd_sum).
    """
    even_sum = 0
    odd_sum = 0

    for value in numbers:
        if value % 2 == 0:
            even_sum += value
        else:
            odd_sum += value

    return even_sum, odd_sum


if __name__ == "__main__":
    try:
        user_input = input("Enter integers separated by spaces (or commas): ").strip()
        if not user_input:
            print("No input provided.")
        else:
            tokens = user_input.replace(',', ' ').split()
            numbers = [int(token) for token in tokens]
            e_sum, o_sum = sum_even_odd(numbers)
            print("Even Sum:", e_sum)
            print("Odd Sum:", o_sum)
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces or commas.")



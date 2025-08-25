def is_valid_indian_mobile(number: str) -> bool:
    """
    Validates an Indian mobile number.
    The number must:
    - Be exactly 10 digits
    - Start with 6, 7, 8, or 9

    Args:
        number (str): The mobile number as a string.

    Returns:
        bool: True if valid, False otherwise.
    """
    return (
        len(number) == 10 and
        number.isdigit() and
        number[0] in {'6', '7', '8', '9'}
    )

# Example usage:
if __name__ == "__main__":
    user_input = input("Enter an Indian mobile number: ")
    if is_valid_indian_mobile(user_input):
        print("Valid Indian mobile number.")
    else:
        print("Invalid Indian mobile number.")
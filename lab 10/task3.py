def calculate_percentage(base_value, percentage):
    """
    Calculate the percentage of a given base value.

    Args:
        base_value (float): The base value.
        percentage (float): The percentage to calculate.

    Returns:
        float: The calculated percentage value.
    """
    return base_value * percentage / 100

# Get user input
try:
    base_value = float(input("Enter the base value: "))  # Prompt user for the base value
    percentage = float(input("Enter the percentage: "))  # Prompt user for the percentage

    # Calculate and print the result
    print(f"The calculated percentage is: {calculate_percentage(base_value, percentage)}")
except ValueError:
    print("Please enter valid numeric values.")

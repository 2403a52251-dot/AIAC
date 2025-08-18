def sort_four_numbers(a, b, c, d):
    """
    Sort four numbers in ascending order.
    
    Args:
        a, b, c, d: Four numbers to be sorted
        
    Returns:
        tuple: Four numbers sorted in ascending order
    """
    # Convert to list and sort
    numbers = [a, b, c, d]
    numbers.sort()
    
    # Return as tuple
    return tuple(numbers)

# Example usage
if __name__ == "__main__":
    # Test the function with different sets of numbers
    print("Sorting 4, 2, 7, 1:", sort_four_numbers(4, 2, 7, 1))
    print("Sorting 10, 5, 3, 8:", sort_four_numbers(10, 5, 3, 8))
    print("Sorting -5, 0, 12, -2:", sort_four_numbers(-5, 0, 12, -2))
    print("Sorting 3.14, 2.71, 1.41, 0.58:", sort_four_numbers(3.14, 2.71, 1.41, 0.58))

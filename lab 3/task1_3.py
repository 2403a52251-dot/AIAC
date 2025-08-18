def factorial(n):
    """
    Calculate the factorial of a non-negative integer n
    n! = n × (n-1) × (n-2) × ... × 2 × 1
    """
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    # Test the function
    print("Factorial Calculator")
    print("=" * 20)
    
    # Test with some numbers
    test_numbers = [0, 1, 5, 10]
    for num in test_numbers:
        result = factorial(num)
        print(f"{num}! = {result}")
    
    # Interactive input
    print("\nEnter a number to calculate its factorial:")
    try:
        user_input = int(input("Number: "))
        result = factorial(user_input)
        print(f"{user_input}! = {result}")
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nGoodbye!")

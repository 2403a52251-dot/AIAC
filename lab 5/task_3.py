def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
    It starts as follows:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n >= 2

    Parameters:
    n (int): The position in the Fibonacci sequence to calculate.

    Returns:
    int: The nth Fibonacci number.
    """
    # Base case: If n is 0, return 0
    if n == 0:
        return 0
    # Base case: If n is 1, return 1
    elif n == 1:
        return 1
    # Recursive case: Calculate the sum of the two preceding Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """
    Main function to prompt user input and display the nth Fibonacci number.
    """
    # Prompt the user to enter the position of the Fibonacci number
    n = int(input("Enter the position (n) of the Fibonacci number: "))
    
    # Validate the input to ensure it is non-negative
    if n < 0:
        print("Error: Please enter a non-negative integer.")
        return
    
    # Call the fibonacci function to calculate the nth Fibonacci number
    result = fibonacci(n)
    
    # Display the result
    print(f"The {n}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()
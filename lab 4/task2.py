def factorial(n):
    """
    Calculates the factorial of a positive integer n.
    Returns an appropriate message if n is negative or not an integer.
    """
    if not isinstance(n, int):
        return "Please enter a valid integer."
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    number = int(input("Enter a positive integer: "))
    print(factorial(number))
except ValueError:
    print("Please enter a valid integer.")
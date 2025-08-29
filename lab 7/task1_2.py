def factr(n):
    # Validate input type and value
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Correct base cases: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1

    # Correct recursion step: decrease by 1 each time
    return n * factr(n - 1)


print(factr(5))


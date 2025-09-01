def sum_to_n(n):
    """
    Calculates the sum of the first n natural numbers using a for loop.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Analysis:
# The sum_to_n function uses a for loop to add each number from 1 to n to the total.
# This is a simple and efficient way to compute the sum.

def sum_to_n_while(n):
    """
    Calculates the sum of the first n natural numbers using a while loop.
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total
if __name__ == "__main__":
    print("Sum using for loop:", sum_to_n(10))      
    print("Sum using while loop:", sum_to_n_while(10)) 
def sum_to_n(n):
    """
    Calculates the sum of the first n natural numbers using a for loop.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Analysis:
# The sum_to_n function uses a for loop to iterate from 1 to n (inclusive),
# adding each number to the total. This is a straightforward and efficient
# way to compute the sum of the first n natural numbers.

# Suggestions for other controlled looping:
# We can also use a while loop to achieve the same result.

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

# Explanation:
# - sum_to_n uses a for loop, which is concise and easy to read for this type of problem.
# - sum_to_n_while uses a while loop, which gives more control over the loop variable and can be useful in situations where the number of iterations is not known in advance.
# Both functions return the sum of the first n natural numbers.

if __name__ == "__main__":
    n = 10
    print(f"Sum of first {n} numbers using for loop:", sum_to_n(n))
    print(f"Sum of first {n} numbers using while loop:", sum_to_n_while(n))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension way - cleaner and more Pythonic
squares = [i * i for i in nums]

# Additional examples of list comprehensions
even_squares = [i * i for i in nums if i % 2 == 0]
cubes = [i ** 3 for i in nums]
strings = [str(i) for i in nums]

print(f"Numbers: {nums}")
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")
print(f"Cubes: {cubes}")
print(f"String numbers: {strings}")

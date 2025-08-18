def print_factorial_of_five() -> None:
	"""Compute and print the factorial of 5."""
	result = 1
	for value in range(2, 6):
		result *= value
	print(result)


if __name__ == "__main__":
	print_factorial_of_five()


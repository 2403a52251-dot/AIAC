def compute_factorial(non_negative_integer: int) -> int:
	"""Return n! for a non-negative integer n."""
	if non_negative_integer < 0:
		raise ValueError("Factorial is undefined for negative integers")
	result = 1
	for value in range(2, non_negative_integer + 1):
		result *= value
	return result


def main() -> None:
	user_input = input("Enter a non-negative integer: ").strip()
	try:
		number = int(user_input)
	except ValueError:
		print("Invalid input. Please enter a non-negative integer.")
		return

	if number < 0:
		print("Invalid input. Please enter a non-negative integer.")
		return

	print(compute_factorial(number))


if __name__ == "__main__":
	main()


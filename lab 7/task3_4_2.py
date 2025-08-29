# Improved number processing using with open() context manager
# This ensures files are automatically closed after use

# Read numbers from file and calculate squares
with open("numbers.txt", "r") as f:
    nums = f.readlines()

# Initialize list to store squares
squares = []

# Process each number and calculate squares
for n in nums:
    n = n.strip()  # Remove whitespace and newlines
    if n.isdigit():  # Check if it's a valid number
        squares.append(int(n) * int(n))

# Write squares to output file
with open("squares.txt", "w") as f2:
    for sq in squares:
        f2.write(str(sq) + "\n")

print("Squares written")

# Alternative approach: Process and write in a single operation
# This is more memory efficient for large files
squares_alt = []
with open("numbers.txt", "r") as input_file:
    for line in input_file:
        n = line.strip()
        if n.isdigit():
            squares_alt.append(int(n) ** 2)  # Using ** operator for cleaner code

with open("squares.txt", "w") as output_file:
    for sq in squares_alt:
        output_file.write(f"{sq}\n")  # Using f-string for cleaner formatting

print("Squares written using alternative approach")

# Most efficient approach: Process line by line without storing all numbers in memory
with open("numbers.txt", "r") as input_file, open("squares.txt", "w") as output_file:
    for line in input_file:
        n = line.strip()
        if n.isdigit():
            square = int(n) ** 2
            output_file.write(f"{square}\n")

print("Squares written using memory-efficient approach")

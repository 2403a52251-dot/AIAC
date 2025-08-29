try:
    # Open the input file and read numbers
    with open("numbers.txt", "r") as f:
        nums = f.readlines()
    
    squares = []
    for n in nums:
        n = n.strip()  # Remove any extra whitespace
        if n.isdigit():  # Check if the line contains a valid number
            squares.append(int(n) ** 2)  # Square the number and add to the list

    # Write the squares to the output file
    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")
    
    print("Squares written successfully.")
except IOError as e:
    print(f"An error occurred while processing the files: {e}")

# filepath: d:\AIAC\lab 7\task3_3_1.py
# Improved version using best practice (with open() block)

with open("input.txt", "r", encoding="utf-8") as input_file, open("output.txt", "w", encoding="utf-8") as output_file:
    for line in input_file:
        output_file.write(line.upper())

print("Processing done. The content of 'input.txt' has been converted to uppercase and written to 'output.txt'.")
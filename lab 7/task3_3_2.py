# Improved file processing using with open() context manager
# This ensures files are automatically closed after use

# Read from input file and process each line
with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Write processed data to output file
with open("output.txt", "w") as output_file:
    for line in data:
        output_file.write(line.upper())

print("Processing done")

# Alternative approach: Process and write in a single operation
# This is more memory efficient for large files
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        output_file.write(line.upper())

print("Processing done using single operation approach")

# Most efficient approach: Process line by line without storing in memory
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        output_file.write(line.upper())

print("Processing done using memory-efficient approach")

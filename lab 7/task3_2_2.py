# Improved file writing using with open() context manager
# This ensures files are automatically closed after use

# Write to first file
with open("data1.txt", "w") as f1:
    f1.write("First file content\n")

# Write to second file
with open("data2.txt", "w") as f2:
    f2.write("Second file content\n")

print("Files written successfully")

# Alternative approach: Write to multiple files in sequence
# This is more efficient if you need to write to many files
files_to_write = [
    ("data1.txt", "First file content\n"),
    ("data2.txt", "Second file content\n")
]

for filename, content in files_to_write:
    with open(filename, "w") as f:
        f.write(content)

print("All files written successfully using loop approach")

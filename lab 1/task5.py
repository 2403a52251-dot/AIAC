def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Static file path
file_path = "example_task.txt" 


# Call the function and print the result
line_count = count_lines_in_file(file_path)
print(f"The file '{file_path}' has {line_count} lines.")
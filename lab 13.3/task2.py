def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except PermissionError:
        raise PermissionError(f"Permission denied to read '{filename}'")
    except Exception as e:
        raise Exception(f"Error reading file '{filename}': {e}")


# Test
if __name__ == "__main__":
    try:
        content = read_file("task2.py")
        print(f"File read successfully: {len(content)} characters")
    except Exception as e:
        print(f"Error: {e}")

def write_message(file_path, message):
    """Write a message to a file using a context manager.

    This ensures the file is properly closed even if an error occurs.
    """
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        file.write(message)


def read_message(file_path):
    """Read and return the file contents using a context manager."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    path = "example.txt"
    write_message(path, "Hello, world!")
    print(read_message(path))



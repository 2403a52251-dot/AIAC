import logging

def write_hello_world(filename="example.txt"):
    """Writes 'Hello, world!' to the specified file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Hello, world!")
    except IOError as e:
        logging.error(f"An error occurred while writing to the file: {e}")
        raise

def main():
    """Entry point for the script."""
    write_hello_world()

if __name__ == "__main__":
    main()
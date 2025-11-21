"""data_parser.py

AI-assisted data processing script that reads a poorly formatted CSV file
containing numbers and calculates their sum.

The script handles:
- Extra whitespace (e.g., "1 , 2" or " 3,4 ")
- Empty entries (e.g., "1,,2")
- Multiple spaces between numbers and commas

Usage:
    python data_parser.py [filename]
    Default filename: data.txt
"""

from typing import List
import sys


def parse_numbers_from_file(filename: str) -> List[int]:
    """Parse integers from a poorly formatted CSV file.

    Reads a file line by line, splits each line by commas, strips whitespace
    from each token, and filters out empty strings. Returns a list of valid
    integers.

    Args:
        filename: Path to the CSV file containing comma-separated values.

    Returns:
        A list of integers parsed from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If a non-empty token cannot be converted to an integer.
    """
    numbers = []

    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                # Split each line by commas
                tokens = line.split(',')

                for token in tokens:
                    # Strip leading and trailing whitespace
                    cleaned_token = token.strip()

                    # Skip empty strings (handles cases like "1,,2")
                    if not cleaned_token:
                        continue

                    try:
                        # Convert to integer and append
                        num = int(cleaned_token)
                        numbers.append(num)
                    except ValueError as e:
                        # Provide helpful error message with line number
                        raise ValueError(
                            f"Line {line_num}: Cannot convert '{cleaned_token}' "
                            f"to integer."
                        ) from e

    except FileNotFoundError:
        raise FileNotFoundError(
            f"File '{filename}' not found. Please ensure the file exists."
        )

    return numbers


def calculate_sum(numbers: List[int]) -> int:
    """Calculate the sum of a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        The sum of all integers in the list.
    """
    return sum(numbers)


def main(filename: str = "data.txt") -> None:
    """Main function to read, parse, and sum numbers from a CSV file.

    Args:
        filename: Path to the CSV file. Defaults to "data.txt".
    """
    try:
        print(f"Reading numbers from '{filename}'...")
        numbers = parse_numbers_from_file(filename)
        total = calculate_sum(numbers)

        print(f"Parsed numbers: {numbers}")
        print(f"Sum of numbers: {total}")

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Allow filename to be passed as a command-line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "data.txt"

    main(filename)

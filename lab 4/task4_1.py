import csv

def analyze_csv(file_path):
    total_rows = 0
    empty_rows = 0
    total_words = 0

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            # Check if all fields are empty or whitespace
            if all(not cell.strip() for cell in row):
                empty_rows += 1
            # Count words in all cells
            for cell in row:
                total_words += len(cell.strip().split())

    return total_rows, empty_rows, total_words
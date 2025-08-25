import csv

def count_rows_and_words(file_path):
    total_rows = 0
    empty_rows = 0
    total_words = 0
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            total_rows += 1
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            total_words += sum(len(cell.split()) for cell in row)
    return total_rows, empty_rows, total_words
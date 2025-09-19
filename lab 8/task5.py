def convert_date_format(date_str):
    """
    Converts a date string from "YYYY-MM-DD" to "DD-MM-YYYY" format.

    Args:
        date_str (str): Date string in "YYYY-MM-DD" format.

    Returns:
        str: Date string in "DD-MM-YYYY" format.
    """
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    yyyy, mm, dd = parts
    return f"{dd}-{mm}-{yyyy}"

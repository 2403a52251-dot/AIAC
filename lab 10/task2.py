#refractor the code with google  style doc string with type hints

def area_of_rectangle(Length: float, Breadth: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        Length (float): The length of the rectangle.
        Breadth (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.
        raise ValueError: If Length or Breadth is negative.
        
    """
    if Length < 0 or Breadth < 0:
        raise ValueError("Length and Breadth must be non-negative.")
    return Length * Breadth



print(area_of_rectangle(10, 20))
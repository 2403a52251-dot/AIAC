import math


def calculate_area(shape, x, y=0):
    area_calculators = {
        "rectangle": lambda: x * y,
        "square": lambda: x * x,
        "circle": lambda: math.pi * x * x
    }
    return area_calculators[shape]()


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


# Test
if __name__ == "__main__":
    print(f"Rectangle: {calculate_area('rectangle', 5, 3)}")
    print(f"Square: {calculate_area('square', 4)}")
    print(f"Circle: {calculate_area('circle', 2)}")

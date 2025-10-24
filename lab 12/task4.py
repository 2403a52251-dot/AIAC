"""
Find minimum value of f(x) = 2x³ + 4x + 5
"""

import math

def f(x):
    """Function: f(x) = 2x³ + 4x + 5"""
    return 2*x**3 + 4*x + 5

def derivative(x):
    """First derivative: f'(x) = 6x² + 4"""
    return 6*x**2 + 4

print("Finding minimum of f(x) = 2x³ + 4x + 5")
print("=" * 40)

# Method 1: Using calculus (find critical points)
print("Method 1: Using calculus")
print("-" * 25)

# Find critical points where f'(x) = 0
# 6x² + 4 = 0
# 6x² = -4
# x² = -4/6 = -2/3
# Since x² cannot be negative, no real critical points exist

print("f'(x) = 6x² + 4")
print("Setting f'(x) = 0:")
print("6x² + 4 = 0")
print("6x² = -4")
print("x² = -2/3")
print("No real solutions (x² cannot be negative)")
print()

# Method 2: Check behavior at different x values
print("Method 2: Checking function behavior")
print("-" * 35)

test_points = [-5, -3, -2, -1, 0, 1, 2, 3, 5]
min_value = float('inf')
min_x = None

print("x\tf(x)")
print("-" * 15)

for x in test_points:
    y = f(x)
    print(f"{x}\t{y}")
    
    if y < min_value:
        min_value = y
        min_x = x

print()
print("=" * 40)
print("RESULTS:")
print(f"Minimum value found: f({min_x}) = {min_value}")

# Method 3: More detailed search
print("\nMethod 3: Detailed search around minimum")
print("-" * 40)

# Search more points around the minimum
detailed_points = []
for x in range(-10, 11):
    detailed_points.append((x, f(x)))

# Find the actual minimum
min_point = min(detailed_points, key=lambda point: point[1])
print(f"Most detailed search: f({min_point[0]}) = {min_point[1]}")

print("\n" + "=" * 40)
print("CONCLUSION:")
print(f"The function f(x) = 2x³ + 4x + 5 has its minimum")
print(f"at x = {min_point[0]} with value f({min_point[0]}) = {min_point[1]}")